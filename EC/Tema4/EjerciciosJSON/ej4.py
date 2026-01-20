# Ejercicio 4 - Caché de API
# Implementa un sistema de caché simple para una API ficticia:
# 1. Crea una función guardar_en_cache(ciudad, datos) que guarde datos en
# cache_{ciudad}.json. Retorna True si todo va bien y False en caso contrario.
# 2. Crea una función cargar_desde_cache(ciudad) que cargue datos si existen. Si
# el archivo no existe, devolver None. Debe retornar los datos de la caché.
# 3. Crea la función mostrar_datos_ciudad, que reciba los datos de caché como
# parámetro de entrada y muestre los datos meteorológicos de la ciudad
# 4. Prueba guardando datos de Madrid y Barcelona
# 5. Verifica que puedes cargar ambos caches

import json
from pathlib import Path

def guardar_en_cache(ciudad, datos):
    try:
        BASE_DIR = Path(__file__).resolve().parent
        fichero = Path(BASE_DIR / f'cache_{ciudad}.json')

        with open(fichero, 'w') as archivo:
            json.dump(datos, archivo)
        return True
    except Exception as e:
        print(f"Error al guardar en caché: {e}")
        return False
    
def cargar_desde_cache(ciudad):
    try:
        BASE_DIR = Path(__file__).resolve().parent
        fichero = Path(BASE_DIR / f'cache_{ciudad}.json')

        with open(fichero, 'r') as archivo:
            datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Error al cargar desde caché: {e}")
        return None

def mostrar_datos_ciudad(datos):
    if datos:
        print(f"Ciudad: {datos['ciudad']}")
        print(f"Temperatura: {datos['temperatura']} °C")
        print(f"Descripción: {datos['descripcion']}")
    else:
        print("No hay datos disponibles.")
# Pista: Estructura de datos
datos_madrid = { 'ciudad': 'Madrid', 'temperatura': 18.5, 'descripcion': 'Soleado' }
guardar_en_cache('madrid', datos_madrid)
cache = cargar_desde_cache('madrid')
print(cache['temperatura']) # 18.5
print("\n3. Mostrando datos de Madrid:")
mostrar_datos_ciudad(cache)