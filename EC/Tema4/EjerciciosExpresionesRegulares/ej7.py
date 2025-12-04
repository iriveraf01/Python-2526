# Ejercicio 7
# Nos dan una lista de frutas y filtrar por aguacate o palta
texto = "platano, manzana, palta, aguacate, pera, aguacate"
import re
coincidencias = re.findall(r"\baguacate\b|\bpalta\b", texto)
print(coincidencias)