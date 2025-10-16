# Ejercicio 3. Haz un programa que pida el nombre y la edad del usuario, y muestre
# cuántos años tendrá dentro de 10 años. Usa input() y f-strings.

nombre, edad = input("Dime tu nombre y tu edad:\n").split(sep=" ")
print(f"Hola {nombre}, tienes {edad} años y dentro de 10 años tendrás {int(edad) + 10} años.")