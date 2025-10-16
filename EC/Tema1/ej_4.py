# Ejercicio 4.
# Crea un programa que:
# 1. Pida al usuario su nombre y apellido.
# 2. Muestre su nombre completo con la primera letra en mayúscula.
# 3. Indique cuántos caracteres tiene su nombre completo.

nombre, apellido = input("Dime tu nombre y tu apellido:\n").split(sep=" ")

print(f"{nombre.title()} {apellido.title()}")
tamaño = len(nombre) + len(apellido)
print(f"El tamaño del nombre completo es de {tamaño}")