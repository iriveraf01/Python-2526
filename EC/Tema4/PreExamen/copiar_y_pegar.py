# Importar clases específicas (recomendado)
from datetime import datetime, date, time, timedelta
# Importar todo el módulo (menos común)
import datetime

import locale
from datetime import datetime
# Configurar localización en español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8') 

hoy = datetime.now()
# self.fecha_creacion = fecha_creacion if fecha_creacion else datetime.now()
# fecha_devolucion = fecha_devolucion if fecha_devolucion else datetime.now()
# meses_diferencia = (hoy.year - self.fecha_publicacion.year) * 12 + (hoy.month - self.fecha_publicacion.month)

# Formato europeo
# El método strptime() (string parse time) es la operación inversa a strftime(): convierte un string a objeto datetime.
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
fecha1 = datetime.strptime("15/03/2025", "%d/%m/%Y")


# Modos de apertura de ESTO with fichero.open('a', encoding='utf-8') as f: PÁGINA 50

# 4.11.1 Lectura de CSV con DictReader (como diccionario) PÁGINA 59

# import json
# datos_python = {
#  'nombre': 'Análisis Ventas Q3',
#  'productos': ['Software', 'Hardware', 'Servicios'],
#  'total_q3': 45000.75,
#  'activo': True
# }
# # Usamos dumps() para obtener la representación JSON como una CADENA de texto.
# json_string = json.dumps(datos_python)
# print(f"Tipo original: {type(datos_python)}")
# print(f"Tipo JSON (string): {type(json_string)}")
# print(json_string)

# El método json.dump() – Guardar en archivo PÁGINA 64-65
# El Método json.load() – Cargar desde archivo PÁGINA 66