DATOS_SUCIOS = [
    "Juan", "Maria", "juan", None, "Ana", 
    "Maria", "Luis", "Ana", "PEDRO", None, 
    "luis", "ana", "Juan"
]
# Ejercicio 2
# Dada una lista de datos que pueden contener información sucia (nombres duplicados,
# formatos inconsistentes, valores None), se necesita limpiarla y analizarla.
# Crea una función analizar_datos(data) que reciba una lista.
# Limpieza: Usa una comprensión de lista con un if para:
# - Eliminar los valores que sean None.
# - Convertir todos los elementos restantes a mayúsculas si son cadenas.
# Análisis:
# Devuelve una tupla que contenga:
# - La lista limpia y normalizada.
# - El conjunto (set) de elementos únicos.
# - El porcentaje de elementos duplicados originales (calculado como
# (total_original - total_unicos) / total_original * 100).
def analizar_datos(data: list) -> tuple:
    normalizados = [nombre.upper() for nombre in DATOS_SUCIOS if nombre != None]
    unicos = set(normalizados)
    porcentaje = (len(normalizados) - len(unicos)) / len(data) * 100
    return (normalizados, unicos, porcentaje)

# Prueba
normalizados, unicos, porcentaje = analizar_datos(DATOS_SUCIOS)

print(f"Datos Normalizados: {normalizados}")
print(f"Elementos Únicos (Set): {unicos}")
print(f"Porcentaje de duplicados: {porcentaje}%") # (5 duplicados / 12 elementos limpios)