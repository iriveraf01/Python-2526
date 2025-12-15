# Ejercicio 5 – Validador de reservas
# Crea un sistema de validación de reservas de hotel:
# 1. Función validar_reserva(fecha_entrada, fecha_salida)
# 2. Verificar que fecha_entrada sea futura (al menos mañana)
# 3. Verificar que fecha_salida sea posterior a fecha_entrada
# 4. Verificar que la estancia sea mínimo 1 noche, máximo 30 noches
# 5. Calcular número de noches y precio (70€/noche entre semana, 100€/noche fin de
# semana)
# 6. Devolver diccionario con: válido (bool), mensaje (str), noches (int), precio_total
# (float)
def validar_reserva(inicio, fin):
    if inicio > fin:
        aux = inicio
        inicio = fin
        fin = aux
    
    while inicio <= fin:
        pass

# Pruebas
print(validar_reserva("07/12/2025", "10/12/2025")) # Válida
print(validar_reserva("05/12/2025", "06/12/2025")) # Entrada debe ser mañana
print(validar_reserva("10/12/2025", "09/12/2025")) # Salida antes de entrada
print(validar_reserva("15/12/2025", "20/01/2026")) # Más de 30 noches