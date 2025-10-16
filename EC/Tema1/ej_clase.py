"""
Pide la edad del usuario y muestra un mensaje según su rango de edad:
- Menor de 12 NIÑO
- Entre 12 y 17 ADOLESCENTE
- Entre 18 y 64 ADULTO
- Mayor de 65 JUBILADO
"""

# nombre, edad = input("Dime tu nombre y tu edad:\n").split(sep=" ")

# if int(edad) < 12:
#     print(f"Eres un niño")
# elif int(edad) <= 17:
#     print(f"Eres un adolescente")
# elif int(edad) <= 64:
#     print(f"Eres un adulto")
# else:
#     print(f"Eres un jubilado")

"""
Que pida un número y muestre su tabla de multiplicar del 1 al 10
"""

# num = int(input("Introduce un número: "))

# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")


"""
Elige un número secreto entre 1 y 10.
"""
# import random

# secreto = random.randint(1, 10)
# num = int(input("Adivina el número secreto entre 1 y 10: "))
# while num != secreto:
#     if num < secreto:
#         print("El número es mayor")
#     else:
#         print("El número es menor")
#     num = int(input("Inténtalo de nuevo: "))
# print("¡Has acertado!")

"""
Pide palabra al usuario y muestra cuantas letras tiene, pero sin contar las vocales
"""

pala = input("Introduce una palabra: ")
contador = 0
for i in pala:
    if i in "aeiouAEIOU":
        contador+=1
print(f"La palabra tiene {len(pala)} letras y sin vocales tiene {contador} letras.")
