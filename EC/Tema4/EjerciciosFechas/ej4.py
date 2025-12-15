# Ejercicio 4 – Dias hasta Enero
# Crea un programa que:
# 1. Pida al usuario una fecha de evento (DD/MM/YYYY)
# 2. Calcule cuántos días faltan para ese evento
# 3. Si el evento ya pasó, mostrar "El evento ya ocurrió hace X días"
# 4. Si el evento es hoy, mostrar "¡El evento es hoy!"
# 5. Si el evento es en el futuro, mostrar "Faltan X días para el evento"
from datetime import datetime, date, time, timedelta
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

def dias_hasta_evento(fecha_evento):
    hoy = datetime.now()
    fecha_objeto = datetime.strptime(fecha_evento, "%d/%m/%Y")
    resta = hoy - fecha_objeto
    if resta.days > 0:
        print(f"El evento ya ocurrió hace {resta.days} días")
    if resta.days == 0:
        print("El evento es hoy!")
    if resta.days < 0:
        print(f"Faltan {resta.days *- 1} días para el evento")

dias_hasta_evento("20/12/2025")