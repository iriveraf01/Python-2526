# Ejercicio 7 – Sistema de logs con fechas
# Un sistema profesional de logs necesita:
# 1. Crear directorio de logs.
# 2. Un archivo por día.
# 3. Añadir timestamps a cada entrada. (nombre: app_2025-12-09.log)
# 4. Modo append para no perder logs anteriores.
# 5. Puedes limpiar logs antiguos buscando archivos con glob() y eliminando los que
# tengan más de X días(usa el nombre del fichero sin extensión(stem) y reemplaza app_
# por “”).
import os
from datetime import datetime, date, time, timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

fichero = Path(BASE_DIR / 'logs')
# 1 Creo el directorio
os.makedirs(fichero, exist_ok=True)

# 2 Archivo por día 
fecha_hoy = date.today()
nombre_fichero = f"app_{fecha_hoy}.log"
fichero_log = fichero / nombre_fichero

# 3 Timestamp y 4 Append
with open(fichero_log, 'a') as f:
    timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    log = f"{timestamp}\n"
    f.write(log)
    print("Ha puesto un log nuevo")

# 5 Limpiar logs antiguos
limite_fecha = fecha_hoy - timedelta(days=1)

for log in fichero.glob("app_*.log"):
    borrar = log.stem.replace("app_", "")
    fecha_log = datetime.strptime(borrar, '%Y-%m-%d').date()
    if fecha_log < limite_fecha:
        log.unlink()
        print("Ha borrado algo")