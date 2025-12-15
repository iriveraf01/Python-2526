# Ejercicio 2
# Crea una función llamada contar_dias_laborales, con parámetros de entrada
# fecha_inicio y fecha_fin que cuente los días laborales (no fin de semana) entre dos
# fechas.
from datetime import datetime, date, time, timedelta
def contar_dias_laborables(inicio, fin):
    dias_laborales = 0

    while inicio <= fin:
        if inicio.weekday() < 5:  # Lunes a viernes
            dias_laborales += 1
        inicio += timedelta(days=1)

    return dias_laborales

#Prueba
inicio = datetime(2025, 12, 1)
fin = datetime(2025, 12, 31)
dias_laborables = contar_dias_laborables(inicio, fin)
print(f"Días laborables en diciembre: {dias_laborables}")