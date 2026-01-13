from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).parent
env_path = BASE_DIR / '.env'

# Cargar las variables del archivo .env
load_dotenv(env_path)

# Ahora acceder con os.getenv()
api_key = os.getenv('API_KEY')
nombre_bd = os.getenv('DB_NAME')
clave_bd = os.getenv('SECRET_KEY')
print(f"API Key: {api_key}")
print(f"Nombre Base de Datos: {nombre_bd}")
print(f"Clave Base de Datos: {clave_bd}")