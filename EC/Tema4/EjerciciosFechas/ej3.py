# Ejercicio 3 - Calcular Edad
# Escribe una función calcular_edad(fecha_nacimiento) que:
# 1. Reciba una fecha de nacimiento como string en formato DD/MM/YYYY
# 2. La convierta a objeto datetime
# 3. Calcule la edad actual en años
# 4. Devuelva un mensaje: "Tienes X años"
# 5. Indique si es mayor o menor de edad
from datetime import datetime, date, time, timedelta
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

def calcular_edad(fecha_nacimiento):
    hoy = datetime.now()
    fecha_objeto = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
    edad = hoy.year - fecha_objeto.year
    if hoy.month < fecha_objeto.month or (hoy.month == fecha_objeto.month and hoy.day < fecha_objeto.day):
        edad -= 1
    
    print(f"Tienes {edad} años")
    
    if edad < 18:
        print("\t - Eres menor de edad.")
    else:
        print("\t - Eres un viejo")

# Pruebas
calcular_edad("15/05/1990")
calcular_edad("01/01/2010")
calcular_edad("20/12/2024") # Recién nacido casi