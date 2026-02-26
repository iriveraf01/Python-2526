from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from dotenv import load_dotenv
from pathlib import Path
import os
import httpx
from fastapi.middleware.cors import CORSMiddleware
import logging

# ─────────────────────────────────────────────
#CARGAR VARIABLES DE ENTORNO
#    load_dotenv() lee el archivo .env
# ─────────────────────────────────────────────
BASE_DIR = Path(__file__).parent       
env_path = BASE_DIR / ".env"           
load_dotenv(env_path)               


api_key   = os.getenv("WEATHER_API_KEY")            
url_base  = str(os.getenv("WEATHER_BASE_URL")) 

# ─────────────────────────────────────────────
#CREAR LA APLICACIÓN FASTAPI
# ─────────────────────────────────────────────
app = FastAPI(
    title="API del Clima",
    description="Consulta el tiempo actual de cualquier ciudad usando OpenWeatherMap",
    version="1.0.0"
)

# ─────────────────────────────────────────────
#Configuracion logger
# ─────────────────────────────────────────────

logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ─────────────────────────────────────────────
#CONFIGURAR CORS (Cross-Origin Resource Sharing)
#    Sin esto, un navegador bloqueará las peticiones
#    que vengan de un dominio distinto al del servidor
#
#    allow_origins=["*"]  → acepta peticiones de cualquier origen
#    allow_methods=["*"]  → acepta GET, POST, PUT, DELETE, etc.
#    allow_headers=["*"]  → acepta cualquier cabecera HTTP
#    allow_credentials=True → permite el envío de cookies/tokens
# ─────────────────────────────────────────────

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# ─────────────────────────────────────────────
# FUNCIÓN obtener_tiempo
# ─────────────────────────────────────────────
@app.get("/api/weather")
async def obtener_tiempo(ciudad: str):
    """
    Devuelve el clima actual de la ciudad indicada.
    - **ciudad**: nombre de la ciudad (ej. Madrid, London, Tokyo)
    """

    if not ciudad:
        raise HTTPException(status_code=400, detail='Debes introducir nombre de ciudad')
    
    
    try: 
        async with httpx.AsyncClient() as client:
            response = await client.get(url_base, 
                                        
                    params={
                    "q":       ciudad,       # Nombre de la ciudad a consultar
                    "appid":   api_key,    # Nuestra clave de API
                    "units":   "metric",   # Unidades métricas → temperatura en °C
                    "lang":    "es"        # Descripciones del clima en español
                    }, timeout=10)

            if response.status_code == 404:
                raise HTTPException(
                    status_code=404,
                    detail=f"Ciudad '{ciudad}' no encontrada. Verifica el nombre e inténtalo de nuevo."
                )

            if response.status_code != 200:
                raise HTTPException(
                    status_code=response.status_code,
                    detail="Error al consultar el servicio meteorológico."
                )

            data = response.json()
            logger.info("Se ha cargado la ciudad :%s", ciudad)
            
            resultado = {
                "ciudad":      data["name"],                        # Nombre oficial de la ciudad
                "temperatura": data["main"]["temp"],                # Temperatura actual en °C
                "sensacion":   data["main"]["feels_like"],          # Sensación térmica en °C
                "humedad":     data["main"]["humidity"],            # Humedad relativa en %
                "descripcion": data["weather"][0]["description"],   # Descripción textual (ej. "lluvia ligera")
                "icono":       data["weather"][0]["icon"],          # Código de icono (úsalo en: https://openweathermap.org/img/wn/{icono}@2x.png)
                "viento":      data["wind"]["speed"]                # Velocidad del viento en m/s
            }

            return resultado
    
    except httpx.TimeoutException as e:
        raise HTTPException(status_code=504, detail='Tiempo de espera agotado') from e
    
# ─────────────────────────────────────────────
# ENDPOINT RAÍZ
#    Ruta de prueba para verificar que el servidor
#    está corriendo correctamente.
# ─────────────────────────────────────────────
@app.get("/")
async def root():
    return {
        "mensaje": "Weather API funcionando correctamente",
        "version": "1.0.0",
        "endpoints": {
            "clima": "/api/weather?ciudad=Madrid"
        }
    }

# ─────────────────────────────────────────────
# EJECUCION
# ─────────────────────────────────────────────
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001)