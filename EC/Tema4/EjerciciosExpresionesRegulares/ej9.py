# Ejercicio 9
# Valida si una cadena sigue el patrón de una matrícula española moderna: 4 dígitos
# seguidos de 3 letras mayúsculas.
# - El patrón debe cubrir toda la cadena (usa ^ y $).
# - Usa \d para los dígitos y [A-Z] para las letras.
# - Usa re.match() o re.search() con los anclajes (^...$) para validar la cadena completa.
matriculas = ["1234ABC", "123AB", "A1234BC"]
import re
patron = r"^\d{4}[A-Z]{3}$"
for i in matriculas:
    correctas = re.search(patron, i)
    print(correctas)