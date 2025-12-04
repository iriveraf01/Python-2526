# Ejercicio 3
# Validar un nombre de usuario (debe comenzar por algo alfanumérico).
texto = "%pepito_123%"
# Si quitamos % del inicio del texto, indicará que el nombre de usuario es válido.
import re
patron = r"^[a-z0-9]"
coincidencia = re.search(patron, texto)
if coincidencia:
    print(f"El nombre de usuario es válido.\n{coincidencia}")
else:
    print("No es válido el nombre usuario.")