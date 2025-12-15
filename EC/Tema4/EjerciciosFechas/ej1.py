# Ejercicio 1
# Crea una función es_fin_de_semana que reciba una fecha y devuelva true si es fin de
# semana. Otra función es_dia_laborable que reciba una fecha y devuelva true si es día
# laborable.  
from datetime import datetime, date, time, timedelta
def es_fin_de_semana(fecha):
    if fecha.weekday() in (5, 6):
        return True


#Prueba
hoy = datetime.now()
fecha_especifica = datetime(2025, 12, 20)
if es_fin_de_semana(fecha_especifica):
    print("¡Es fin de semana!")
else:
    print("Es día laborable")