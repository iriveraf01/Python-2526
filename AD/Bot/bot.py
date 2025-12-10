from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from datetime import date, timedelta
import acceso_datos
import logging
from config import TOKEN

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def formatear_mensaje(humedad: dict, temp: dict):
    return (
        f"Humedad relativa del ambiente (%)\n"
        f"  - Media: {humedad['mean']}\n"
        f"  - Min: {humedad['min']}\n"
        f"  - Max: {humedad['max']}\n"
        f"Temperatura relativa del ambiente (°C)\n"
        f"  - Media: {temp['mean']}\n"
        f"  - Min: {temp['min']}\n"
        f"  - Max: {temp['max']}\n"
    )

def validar_ubicacion(args: list[str]):
    if not args or len(args) > 1:
        return None
    ubic = args[0].lower()
    return ubic if ubic in ['huerto', 'invernadero'] else None


async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Bot de Monitoreo Ambiental\n\n"
        "Comandos disponibles (requieren ubicación: 'huerto' o 'invernadero'):\n"
        "/actual [ubicacion]: Muestra valores actuales\n"
        "/diario [ubicacion]: Muestra resumen del día anterior\n"
        "/semanal [ubicacion]: Muestra resumen de la semana\n"
        "/consejo [ubicacion]: Consejo de Gemini"
    )
    await update.message.reply_text(text)


async def diario_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    ubicacion = validar_ubicacion(context.args)

    if not ubicacion:
        await context.bot.send_message(chat_id=chat_id, text="Ubicación no válida. Usa huerto o invernadero.")
        return

    ayer = (date.today() - timedelta(days=1)).strftime('%Y-%m-%d')

    await context.bot.send_message(chat_id=chat_id, text=f"Consultando datos del {ubicacion} de {ayer}...")

    if ubicacion == "huerto":
        datos = acceso_datos.diario_huerto_humedad()
        datos_temp = acceso_datos.diario_huerto_temperatura()
    else:  # invernadero
        datos = acceso_datos.diario_invernadero_humedad()
        datos_temp = acceso_datos.diario_invernadero_temperatura()

    texto = formatear_mensaje(datos, datos_temp)
    await context.bot.send_message(chat_id=chat_id, text=texto)


def main():
    appbot = ApplicationBuilder().token(TOKEN).build()

    appbot.add_handler(CommandHandler("menu", menu_handler))
    appbot.add_handler(CommandHandler("diario", diario_handler))

    appbot.run_polling()


if __name__ == '__main__':
    main()
