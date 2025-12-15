import logging
import json
from datetime import date, timedelta, datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import acceso_datos
import config
from google import genai

# =================================================================
# ACTIVACIÓN DEL LOG
# =================================================================
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# =================================================================
# CONFIGURACIÓN DE API TOKENS
# =================================================================
TOKEN_BOT = config.TOKEN_BOT
GEMINI_API_KEY = config.GEMINI_API_KEY

# =================================================================
# FUNCIONES AUXILIARES PARA FORMATEAR MENSAJES PARA TELEGRAM
# =================================================================
def formatear_mensaje(temp, humedad):
    return (
        "🌡️Temperatura (°C):\n"
        f"   • Media: {temp['mean']}\n"
        f"   • Min: {temp['min']}\n"
        f"   • Max: {temp['max']}\n"
        
        "💧Humedad Relativa (%):\n"
        f"   • Media: {humedad['mean']}\n"
        f"   • Min: {humedad['min']}\n"
        f"   • Max: {humedad['max']}\n"
    )

def formatear_mensaje_actual(temp, humedad):
    return (
        f"🌡️Temperatura: {temp['value']}°C\n"
        f"💧Humedad Relativa: {humedad['value']}%\n"
    )

# =================================================================
# FUNCIÓN PARA PEDIR CONSEJO A GEMINI
# =================================================================
def consejo_gemini(datos_sensores: str, zona: str, planta: str) -> dict:
    """
    Solicita a Gemini una valoración del estado y decisión de riego.
    Retorna un diccionario con la respuesta parseada o un mensaje de error.
    """
    client = genai.Client(api_key=GEMINI_API_KEY)

    prompt = f"""
            Eres un sistema inteligente de control automático de riego para agricultura doméstica.

            CONTEXTO:
            - Ubicación: {zona}
            - Tipo de planta: {planta}
            - Sistema: riego automático simulado

            DATOS DE LOS SENSORES:
            {datos_sensores}

            OBJETIVOS:
            1. Evaluar el estado general del {zona} en función de la planta indicada ({planta}).
            2. Analizar si las condiciones actuales son adecuadas para dicha planta.
            3. Decidir si es necesario activar o desactivar el riego (simulado).
            4. Proporcionar una valoración clara basada en los datos.

            REGLAS:
            - No inventes datos.
            - Basa la decisión de riego principalmente en la humedad relativa.
            - Sé conservador con el riego: solo activa si realmente es necesario.
            - Supón un entorno doméstico.
            - La salida será usada por un sistema automático.

            FORMATO DE RESPUESTA (OBLIGATORIO):
            Devuelve EXCLUSIVAMENTE un JSON válido con la siguiente estructura:

            {{
                "estado_general": "óptimo | aceptable | crítico",
                "valoracion": "breve explicación del estado del cultivo según la planta",
                "accion_riego": "activar | desactivar",
                "motivo_riego": "justificación breve de la decisión"
            }}

            No incluyas ningún texto fuera del JSON. No uses bloques de código markdown.
            """
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        # Extraer el texto de la respuesta
        texto_respuesta = response.text.strip()
        
        # Limpiar posibles bloques de código markdown
        if texto_respuesta.startswith("```"):
            # Eliminar ```json y ``` si existen
            texto_respuesta = texto_respuesta.replace("```json", "").replace("```", "").strip()
        
        # Parsear JSON
        resultado = json.loads(texto_respuesta)
        
        # Validar que tenga las claves esperadas
        claves_requeridas = ["estado_general", "valoracion", "accion_riego", "motivo_riego"]
        if not all(clave in resultado for clave in claves_requeridas):
            return {
                "error": True,
                "mensaje": "La respuesta de Gemini no tiene el formato esperado."
            }
        
        return resultado
        
    except json.JSONDecodeError as e:
        logging.error(f"Error al parsear JSON de Gemini: {e}")
        logging.error(f"Respuesta recibida: {response.text if 'response' in locals() else 'No disponible'}")
        return {
            "error": True,
            "mensaje": f"Error al interpretar la respuesta de Gemini (JSON inválido)."
        }
    except Exception as e:
        logging.error(f"Error en API de Gemini: {e}")
        return {
            "error": True,
            "mensaje": f"Error de conexión con Gemini: {str(e)}"
        }


# =================================================================
# VALIDACIÓN DE ARGUMENTO UBICACIÓN
# =================================================================
def validar_ubicacion(args: list[str]) -> str:
    """Valida que la ubicación del comando sea correcta y no tenga más argumentos."""
    if not args or len(args) > 1 or args[0].lower() not in ["huerto", "invernadero"]:
        return "" 
    
    return args[0].lower()

# =================================================================
# MANEJADORES DE CADA COMANDO DEL BOT TELEGRAM
# =================================================================

# /menu
async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /menu para mostrar ayuda."""
    ayuda_mensaje = (
        "🌱 Bot de Monitoreo Ambiental\n\n"
        "👨‍💻 Comandos disponibles:\n\n"
        "➡️ /actual huerto o invernadero.\n"
        "   Muestra valores actuales\n\n"
        "➡️ /diario huerto o invernadero.\n"
        "   Resumen del día anterior\n\n"
        "➡️ /semanal huerto o invernadero.\n"
        "   Resumen de la última semana\n\n"
        "➡️ /historico huerto 48\n"
        "   Histórico de las últimas horas\n\n"
        "➡️ /comparar\n"
        "   Compara huerto e invernadero\n\n"
        "➡️ /consejo huerto tomate\n"
        "   Consejo IA y control de riego"
    )

    await update.message.reply_text(ayuda_mensaje)


# /diario <ubicación>
async def diario_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /diario [ubicacion]."""
    chat_id = update.effective_chat.id
    
    # 1. Validar Ubicación
    ubicacion = validar_ubicacion(context.args)
    if not ubicacion:
        error = f"❌ Ubicación no válida. Usa 'huerto' o 'invernadero'.\nEj: /diario huerto"
        await context.bot.send_message(chat_id=chat_id, text=error)
        return
    
    # 2. Obtenemos Fecha actual para mostrarla
    hoy = date.today()
    ayer = hoy - timedelta(days=1)
    fecha = f"{ayer.strftime('%Y-%m-%d')}"    
    await context.bot.send_message(chat_id=chat_id, text=f"🔍 Consultando datos del {ubicacion} de {fecha}.")

    # 3. Obtenemos los datos
    if ubicacion == 'huerto':
        humedad = acceso_datos.diario_huerto_humedad()
        temp = acceso_datos.diario_huerto_temperatura()
    else: 
        # Solo hay opcion de que sea invernadero
        humedad = acceso_datos.diario_invernadero_humedad()
        temp = acceso_datos.diario_invernadero_temperatura()
        
    # 4. Formateamos el mensaje
    mensaje = formatear_mensaje(temp, humedad)
    
    # 5. Enviar la respuesta
    await context.bot.send_message(chat_id=chat_id, text=mensaje)

# /semanal <ubicación>
async def semanal_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /semanal [ubicacion]."""
    chat_id = update.effective_chat.id

    # 1. Validar Ubicación
    ubicacion = validar_ubicacion(context.args)
    if not ubicacion:
        error = "❌ Ubicación no válida. Usa 'huerto' o 'invernadero'.\nEj: /semanal huerto"
        await context.bot.send_message(chat_id=chat_id, text=error)
        return

    # 2. Rango de fechas (últimos 7 días)
    hoy = date.today()
    inicio = hoy - timedelta(days=7)
    rango = f"{inicio.strftime('%Y-%m-%d')} → {hoy.strftime('%Y-%m-%d')}"

    await context.bot.send_message(
        chat_id=chat_id,
        text=f"📊 Consultando resumen semanal del {ubicacion}\n🗓️ {rango}"
    )

    # 3. Obtener datos según ubicación
    if ubicacion == "huerto":
        temp = acceso_datos.semanal_huerto_temperatura()
        humedad = acceso_datos.semanal_huerto_humedad()
    else:  # invernadero
        temp = acceso_datos.semanal_invernadero_temperatura()
        humedad = acceso_datos.semanal_invernadero_humedad()

    # 4. Formatear mensaje
    mensaje = formatear_mensaje(temp, humedad)

    # 5. Enviar respuesta
    await context.bot.send_message(chat_id=chat_id, text=mensaje)


# /actual <ubicación>
async def actual_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /actual [ubicacion]."""
    chat_id = update.effective_chat.id

    # 1. Validar Ubicación
    ubicacion = validar_ubicacion(context.args)
    if not ubicacion:
        error = "❌ Ubicación no válida. Usa 'huerto' o 'invernadero'.\nEj: /actual huerto"
        await context.bot.send_message(chat_id=chat_id, text=error)
        return

    # 2. Mensaje informativo
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M")
    await context.bot.send_message(
        chat_id=chat_id,
        text=f"📡 Consultando valores actuales del {ubicacion} ({ahora})..."
    )

    # 3. Obtener datos según ubicación
    if ubicacion == "huerto":
        temp = acceso_datos.actual_huerto_temperatura()
        humedad = acceso_datos.actual_huerto_humedad()
    else:  # invernadero
        temp = acceso_datos.actual_invernadero_temperatura()
        humedad = acceso_datos.actual_invernadero_humedad()

    # 4. Formatear mensaje
    mensaje = formatear_mensaje_actual(temp, humedad)

    # 5. Enviar respuesta
    await context.bot.send_message(chat_id=chat_id, text=mensaje)


# /consejo <ubicación> <planta>
async def consejo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Valoración del estado y simulación de riego usando IA."""
    chat_id = update.effective_chat.id

    # 1. Validar argumentos
    if len(context.args) < 2:
        await context.bot.send_message(
            chat_id=chat_id,
            text="❌ Uso incorrecto.\n\n"
                "Formato correcto:\n"
                "`/consejo [ubicación] [planta]`\n\n"
                "Ejemplo:\n"
                "`/consejo huerto tomate`\n"
                "`/consejo invernadero pimiento`",
            parse_mode="Markdown"
        )
        return

    ubicacion = validar_ubicacion([context.args[0]])
    planta = " ".join(context.args[1:])  # Permite plantas con espacios

    if not ubicacion:
        await context.bot.send_message(
            chat_id=chat_id,
            text="❌ Ubicación no válida. Usa 'huerto' o 'invernadero'.\n\n"
                "Ejemplo: `/consejo huerto tomate`",
            parse_mode="Markdown"
        )
        return

    await context.bot.send_message(
        chat_id=chat_id,
        text=f"🤖 Analizando el *{ubicacion}* para la planta: *{planta}*...\n"
            f"⏳ Consultando sensores y obteniendo valoración de IA...",
        parse_mode="Markdown"
    )

    # 2. Obtener datos actuales
    try:
        if ubicacion == "huerto":
            temp = acceso_datos.actual_huerto_temperatura()
            humedad = acceso_datos.actual_huerto_humedad()
        else:
            temp = acceso_datos.actual_invernadero_temperatura()
            humedad = acceso_datos.actual_invernadero_humedad()
    except Exception as e:
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"❌ Error al obtener datos de sensores: {str(e)}"
        )
        return

    # 3. Preparar datos para la IA
    datos_sensores = (
        f"Temperatura actual: {temp['value']} °C\n"
        f"Humedad relativa actual: {humedad['value']} %"
    )

    # 4. Llamar a Gemini
    respuesta_ia = consejo_gemini(
        datos_sensores=datos_sensores,
        zona=ubicacion,
        planta=planta
    )

    # 5. Procesar respuesta
    if respuesta_ia.get("error"):
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"❌ {respuesta_ia.get('mensaje', 'Error desconocido')}"
        )
        return

    # 6. Formatear respuesta estructurada
    estado = respuesta_ia.get("estado_general", "desconocido").upper()
    valoracion = respuesta_ia.get("valoracion", "Sin valoración")
    accion = respuesta_ia.get("accion_riego", "desactivar")
    motivo = respuesta_ia.get("motivo_riego", "Sin motivo especificado")

    # Emojis según el estado
    emoji_estado = {
        "ÓPTIMO": "✅",
        "ACEPTABLE": "⚠️",
        "CRÍTICO": "🚨"
    }.get(estado, "ℹ️")

    # Emoji y texto según acción de riego
    if accion.lower() == "activar":
        emoji_riego = "💧"
        texto_riego = "👍 RIEGO ACTIVADO"
    else:
        emoji_riego = "🚫"
        texto_riego = "👎 RIEGO DESACTIVADO"

    mensaje_final = (
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"📊 *VALORACIÓN DEL SISTEMA*\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📍 *Ubicación:* {ubicacion.capitalize()}\n"
        f"🌱 *Planta:* {planta.capitalize()}\n"
        f"🌡️ *Temperatura:* {temp['value']}°C\n"
        f"💧 *Humedad:* {humedad['value']}%\n\n"
        f"{emoji_estado} *Estado General:* {estado}\n"
        f"📝 *Valoración:*\n{valoracion}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"{emoji_riego} *CONTROL DE RIEGO*\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🎯 *Acción:* {texto_riego}\n"
        f"💬 *Motivo:*\n{motivo}\n"
        f"━━━━━━━━━━━━━━━━━━━━━"
    )

    # 7. Enviar respuesta
    await context.bot.send_message(
        chat_id=chat_id,
        text=mensaje_final,
        parse_mode="Markdown"
    )

# /comparar [actual|diario]
async def comparar_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Compara huerto vs invernadero (valores actuales o diarios)."""
    chat_id = update.effective_chat.id

    # 1. Validar tipo de comparación (por defecto: actual)
    tipo = "actual"
    if context.args and len(context.args) == 1:
        tipo_arg = context.args[0].lower()
        if tipo_arg not in ["actual", "diario"]:
            await context.bot.send_message(
                chat_id=chat_id,
                text="❌ Tipo no válido. Usa 'actual' o 'diario'.\n\n"
                    "Ejemplos:\n"
                    "`/comparar` (por defecto: actual)\n"
                    "`/comparar actual`\n"
                    "`/comparar diario`",
                parse_mode="Markdown"
            )
            return
        tipo = tipo_arg
    elif context.args and len(context.args) > 1:
        await context.bot.send_message(
            chat_id=chat_id,
            text="❌ Demasiados argumentos.\n\n"
                "Uso: `/comparar [actual|diario]`",
            parse_mode="Markdown"
        )
        return

    # 2. Mensaje informativo
    tipo_texto = "actuales" if tipo == "actual" else "del día anterior"
    await context.bot.send_message(
        chat_id=chat_id,
        text=f"🔍 Comparando valores {tipo_texto} entre huerto e invernadero..."
    )

    # 3. Obtener datos según el tipo
    try:
        if tipo == "actual":
            # Datos actuales
            huerto_temp = acceso_datos.actual_huerto_temperatura()
            huerto_hum = acceso_datos.actual_huerto_humedad()
            inv_temp = acceso_datos.actual_invernadero_temperatura()
            inv_hum = acceso_datos.actual_invernadero_humedad()
            
            # Extraer valores
            h_temp = huerto_temp['value']
            h_hum = huerto_hum['value']
            i_temp = inv_temp['value']
            i_hum = inv_hum['value']
            
        else:  # diario
            # Datos diarios (medias)
            huerto_temp = acceso_datos.diario_huerto_temperatura()
            huerto_hum = acceso_datos.diario_huerto_humedad()
            inv_temp = acceso_datos.diario_invernadero_temperatura()
            inv_hum = acceso_datos.diario_invernadero_humedad()
            
            # Extraer medias
            h_temp = huerto_temp['mean']
            h_hum = huerto_hum['mean']
            i_temp = inv_temp['mean']
            i_hum = inv_hum['mean']
            
    except Exception as e:
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"❌ Error al obtener datos: {str(e)}"
        )
        return

    # 4. Calcular diferencias
    diff_temp = i_temp - h_temp
    diff_hum = i_hum - h_hum

    # 5. Formatear símbolos de diferencia
    simbolo_temp = "+" if diff_temp > 0 else ""
    simbolo_hum = "+" if diff_hum > 0 else ""

    # 6. Determinar cuál tiene mejores condiciones
    mejor_ubicacion = ""
    razon = ""
    
    # Lógica simple: temperatura moderada (20-25°C) y humedad media-alta (50-80%) son ideales
    score_huerto = 0
    score_inv = 0
    
    # Evaluar temperatura (ideal: 20-25°C)
    if 20 <= h_temp <= 25:
        score_huerto += 2
    elif 15 <= h_temp < 20 or 25 < h_temp <= 30:
        score_huerto += 1
        
    if 20 <= i_temp <= 25:
        score_inv += 2
    elif 15 <= i_temp < 20 or 25 < i_temp <= 30:
        score_inv += 1
    
    # Evaluar humedad (ideal: 50-80%)
    if 50 <= h_hum <= 80:
        score_huerto += 2
    elif 40 <= h_hum < 50 or 80 < h_hum <= 90:
        score_huerto += 1
        
    if 50 <= i_hum <= 80:
        score_inv += 2
    elif 40 <= i_hum < 50 or 80 < i_hum <= 90:
        score_inv += 1
    
    if score_huerto > score_inv:
        mejor_ubicacion = "🏆 Huerto"
        razon = "Condiciones más equilibradas"
    elif score_inv > score_huerto:
        mejor_ubicacion = "🏆 Invernadero"
        razon = "Condiciones más equilibradas"
    else:
        mejor_ubicacion = "⚖️ Empate"
        razon = "Condiciones similares"

    # 7. Crear mensaje formateado
    titulo = "📊 COMPARATIVA ACTUAL" if tipo == "actual" else "📊 COMPARATIVA DIARIA"
    fecha_info = ""
    if tipo == "diario":
        ayer = date.today() - timedelta(days=1)
        fecha_info = f"📅 {ayer.strftime('%Y-%m-%d')}\n\n"
    
    mensaje = (
        f"{titulo}\n"
        f"{'━' * 30}\n\n"
        f"{fecha_info}"
        f"🌾 *Huerto*\n"
        f"   🌡️ {h_temp}°C  |  💧 {h_hum}%\n\n"
        f"🏠 *Invernadero*\n"
        f"   🌡️ {i_temp}°C  |  💧 {i_hum}%\n\n"
        f"{'━' * 30}\n"
        f"📊 *DIFERENCIAS*\n"
        f"{'━' * 30}\n\n"
        f"🌡️ Temperatura: {simbolo_temp}{diff_temp:.1f}°C\n"
        f"💧 Humedad: {simbolo_hum}{diff_hum:.1f}%\n\n"
        f"{'━' * 30}\n"
        f"{mejor_ubicacion}\n"
        f"💡 {razon}"
    )

    # 8. Enviar respuesta
    await context.bot.send_message(
        chat_id=chat_id,
        text=mensaje,
        parse_mode="Markdown"
    )

    # /historico <ubicación> <horas>
async def historico_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    # Validar argumentos
    if len(context.args) != 2:
        await context.bot.send_message(
            chat_id=chat_id,
            text="❌ Uso incorrecto.\n\n"
                "Formato:\n"
                "`/historico <ubicación> <horas>`\n\n"
                "Ejemplo:\n"
                "`/historico huerto 48`",
            parse_mode="Markdown"
        )
        return

    ubicacion = validar_ubicacion([context.args[0]])
    
    if not ubicacion:
        await context.bot.send_message(
            chat_id=chat_id,
            text="❌ Ubicación no válida. Usa 'huerto' o 'invernadero'."
        )
        return

    try:
        horas = int(context.args[1])
        if horas <= 0 or horas > 720:
            raise ValueError
    except ValueError:
        await context.bot.send_message(
            chat_id=chat_id,
            text="❌ El número de horas debe ser un entero entre 1 y 720."
        )
        return

    await context.bot.send_message(
        chat_id=chat_id,
        text=f"📅 Consultando histórico de las últimas {horas}h ({ubicacion})..."
    )

    # Obtener datos
    if ubicacion == "huerto":
        temp = acceso_datos.historico_huerto_temperatura(horas)
        humedad = acceso_datos.historico_huerto_humedad(horas)
    else:
        temp = acceso_datos.historico_invernadero_temperatura(horas)
        humedad = acceso_datos.historico_invernadero_humedad(horas)

    if not temp or not humedad:
        await context.bot.send_message(
            chat_id=chat_id,
            text="⚠️ No hay datos suficientes para ese rango."
        )
        return

    # Formatear y enviar
    mensaje = (
        f"📊 *HISTÓRICO ÚLTIMAS {horas} HORAS*\n"
        f"{'━' * 30}\n"
        f"{formatear_mensaje(temp, humedad)}"
    )

    await context.bot.send_message(
        chat_id=chat_id,
        text=mensaje,
        parse_mode="Markdown"
    )


# =================================================================
# FUNCIÓN PRINCIPAL Y REGISTRO DE MANEJADORES
# =================================================================
def main():
    if not TOKEN_BOT:
        print("ERROR: Por favor, reemplaza 'TOKEN' en el archivo config.py.")
        return

    # Se crea la clase que controla del Bot con el TOKEN
    appbot = ApplicationBuilder().token(TOKEN_BOT).build()

    # Registro de funciones manejadoras de comandos
    appbot.add_handler(CommandHandler("menu", menu_handler))
    appbot.add_handler(CommandHandler("diario", diario_handler))
    appbot.add_handler(CommandHandler("actual", actual_handler))
    appbot.add_handler(CommandHandler("semanal", semanal_handler))
    appbot.add_handler(CommandHandler("consejo", consejo_handler))
    appbot.add_handler(CommandHandler("comparar", comparar_handler))
    appbot.add_handler(CommandHandler("historico", historico_handler))

    # Se inicia el sondeo de comandos a servidores de Telegram
    print("El bot de monitoreo está corriendo...")
    appbot.run_polling()

if __name__ == '__main__':
    main()