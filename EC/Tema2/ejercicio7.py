# Ejercicio 7
# Crea un programa que pida números al usuario y calcule su suma. El programa termina
# cuando el usuario introduce un número vacío. Usa el operador morsa.

suma = 0
while (n := input("Introduce un número: ")) != "":
    numero = int(n)
    suma += numero
print(f"La suma total es de: {suma}")