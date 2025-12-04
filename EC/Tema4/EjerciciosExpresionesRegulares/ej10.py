# Ejercicio 10
# Reemplazar todos los caracteres que no sean letras o espacios por un guion bajo (_).
# - Usa el conjunto de caracteres negado [^...] para capturar todo lo que NO sea letra o
# espacio.
# - Usa re.sub().
cadena_sucia = "Archivo_Final-V1.0.txt (Copia)"
import re
patron = r"[^A-Za-z ]+"
cadena_limpia = re.sub(patron, "_", cadena_sucia)
print(cadena_limpia)