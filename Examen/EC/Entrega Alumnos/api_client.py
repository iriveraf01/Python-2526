from pathlib import Path
import os
from datetime import datetime
from typing import Optional, Dict
import requests
from dotenv import load_dotenv


class ClienteClimaAPI:

    try:
        BASE_DIR = Path(__file__).parent
        env_path = BASE_DIR / ".env"
        # Cargar las variables del archivo .env
        load_dotenv(env_path)
        # Ahora acceder con os.getenv()
        api_key = os.getenv('API_KEY')
        url_base = os.getenv('URL_OPENWEATHER')
        ciudad_defecto = os.getenv('CIUDAD_DEFECTO')
        unidades = os.getenv('UNIDADES')
    except ValueError:
        print("Variable de entorno API_KEY no encontrada. Configúrala en el archivo .env")
    def __init__(self, api_key=api_key, url_base=url_base, ciudad_defecto=ciudad_defecto, unidades=unidades):
        self.api_key = api_key
        self.url_base = url_base
        self.ciudad_defecto = ciudad_defecto
        self.unidades = unidades

    print("Cliente API inicializado:\n"
        f"\t- Ciudad por defecto: {ciudad_defecto}\n"
        f"\t- Unidades: {unidades}\n")
    
    def obtener_clima_actual(self, ciudad:Optional[str] = None) -> Optional[Dict]:
        ciudad = ciudad if ciudad else self.ciudad_defecto
        params = {
            'q':ciudad,
            'appid':self.api_key,
            'units':self.unidades,
            'lang':'es'
        }
        respuesta = requests.get(self.url_base, params, timeout=10)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            ciudad:str = datos['name']
            temperatura:float = datos['main']['temp']
            sensacion_termica:float = datos['main']['feels_like']
            descripcion:str = datos['weather'][0]['description']
            humedad:int = datos['main']['humidity']
            timestamps:str = datetime.now().isoformat()

            return {
                "Ciudad": ciudad,
                "Temperatura": temperatura,
                "Sensación térmica": sensacion_termica,
                "Descripción" : descripcion,
                "Humedad" : humedad,
                "Timestamps" : timestamps
            }


#PRUEBAS
if __name__ == "__main__":
    cliente_api = ClienteClimaAPI()
    clima_actual = cliente_api.obtener_clima_actual()
    print(clima_actual)

    # cliente_api = ClienteClimaAPI()
    # clima_actual = cliente_api.obtener_clima_actual("Zafra")
    # print(clima_actual)
        