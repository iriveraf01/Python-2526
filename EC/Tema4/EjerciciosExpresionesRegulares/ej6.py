# Ejercicio 6
# En el siguiente texto, filtrar la palabra “casa”.
texto = "casa casado casada"
import re
coincidencias = re.findall(r"\bcasa\b", texto)
print(coincidencias)
