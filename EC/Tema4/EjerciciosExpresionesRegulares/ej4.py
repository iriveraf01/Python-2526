# Ejercicio 4
# Validar si la cadena acaba con mundo.
texto = "Hola mundo"
import re
coincidencia = re.search(r'mundo$', texto)
if coincidencia:
    print(f"Acaba en mundo\n{coincidencia}")
else:
    print("No acaba en mundo.")
