# Ejercicio 1
# Encuentra la primera ocurrencia de la palabra “IA” en el siguiente texto e indica en qué
# posición empieza y termina la coincidencia.
import re 
texto = "Todo el mundo dice que la IA nos va a quitar el trabajo. " \
"Pero solo hace falta ver cómo la puede cagar con Las Regex para ir con cuidado"
patron = r"IA"
resultado = re.search(patron, texto)
print(f"{resultado.group(0)} aparece en la posición {resultado.start()} y termina la coincidencia en {resultado.end()}")