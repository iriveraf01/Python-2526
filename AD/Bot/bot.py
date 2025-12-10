from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from datetime import date, datetime, timedelta
import acceso_datos
import logging
from config import TOKEN
# ====================
# Configuración básica
# ====================
logging.basicConfig(format='%(asctime)s- %(name)s $(levelname)s - %(message)s', level=logging.INFO)


def formatear_mensaje(humedad, temp):
    return(
        f'Humedad relativa del ambiente (%)\n'
        f'  - Media: {humedad['media']}\n'
        f'  - Min: {humedad['minimo']}\n'
        f'  - Max: {humedad['maximo']}\n'
        f'Temperatura relativa del ambiente (°C)\n'
        f'  - Media: {temp['media']}\n'
        f'  - Min: {temp['minimo']}\n'
        f'  - Max: {temp['maximo']}\n'
    )

def validar_ubicacion(args: list[str]):
    if not args or len(args) > 1 or args[0].lower() not in ['huerto', 'invernadero']:
        return ""
    else:
        return args[0].lower()

# =======================
# MANEJADORES DE COMANDOS
# =======================

# Comando menu
async def menu_handler(update: Update, context:ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text = {
        "Bot de Monitoreo Ambiental\n\n"
        "Comandos diponibles (requieren ubicación: 'huerto' o 'invernadero'):\n"
        "/actual [ubicacion]: Muestra valores actuales\n"
        "/diario [ubicacion]: Muestra resumen del día anterior\n"
        "/semanal [ubicacion]: Muestra resumen de la semana\n"
        "/consejo [ubicacion]: Consejo de Gemini"
    }
    await context.bot.send_message(chat_id=chat_id, text=text)

# Comando /diario humedad
# Comando /diario invernadero
async def diario_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    ubicacion = validar_ubicacion(context.args)
    if not ubicacion:
        await context.bot.send_message(chat_id=chat_id, text="Ubicación no válida. Usa huerto o invernadero.")
    else:
        hoy = date.today()
        ayer = hoy - timedelta(days=1)
        fecha = ayer.strftime('%Y-%m-%d')
        await context.bot.send_message(chat_id=chat_id, text=f"Consultando datos del {ubicacion} de {fecha}")
        if ubicacion == "huerto":
            datos = acceso_datos.diario_huerto_humedad()
            datos_temp = acceso_datos.diario_huerto_temperatura()
            texto = formatear_mensaje(datos, datos_temp)
            await context.bot.send_message(chat_id=chat_id, text=texto)

def main():
    appbot = ApplicationBuilder().token(TOKEN).build()

    appbot.add_handler(CommandHandler("diario", diario_handler))
    appbot.add_handler(CommandHandler("menu", menu_handler))
    appbot.run_polling()

if __name__ == '__main__':
    main()