# Ejercicio 8
# Extraer todas las fechas que sigan el formato DD/MM/AAAA de una cadena de texto.
# Usa el patrón: \d{2}/\d{2}/\d{4}. Utiliza re.findall().
texto_agenda = "La reunión es el 05/11/2025. La fecha límite era el 30/10/2025, no el 1/1/2025."
patron = r"\d{2}/\d{2}/\d{4}"

import re
coincidencias = re.findall(patron, texto_agenda)
print(f"Las fechas de la agenda son:\n{coincidencias}")