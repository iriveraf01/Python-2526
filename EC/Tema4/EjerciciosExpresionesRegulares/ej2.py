# Ejercicio 2
# Encontrar si en la cadena hay un número de España.
import re
texto = "Mi número de teléfono es +34 678475673 y el de portugal es +35 656748392"
patron = r".34 \d{9}"
tlfno = re.findall(patron, texto)
print(tlfno)