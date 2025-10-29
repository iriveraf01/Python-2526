# Ejercicios tuplas
# Ejercicio 1
# Crea una tupla con tres nombres de personas. Accede al segundo nombre y
# muéstralo por pantalla.
nombres = ("Ana", "Luis", "María")
print(nombres[1])
# Ejercicio 2
# Crea una tupla con los números del 1 al 5. Usa un bucle for para mostrar
# todos sus elementos uno por uno.
numeros = (1, 2, 3, 4, 5)
for i in numeros:
    print(i, end=" ")
# Ejercicio 3
# Dada la siguiente tupla: datos = ("Juan", 25, "España")
# Desempaquétala en tres variables y muestra un mensaje como:
# Juan tiene 25 años y vive en España.
datos = ("Juan", 25, "España")
nombre, edad, pais = datos
print(f"\n{nombre} tiene {edad} años y vive en {pais}")
# Ejercicio 4
# Dada la tupla siguiente: numeros = (4, 2, 4, 1, 4, 3, 2)
# Cuenta cuántas veces aparece el número 4 y muestra el resultado por pantalla.
numeros = (4, 2, 4, 1, 4, 3, 2)
print(numeros.count(4))
# Ejercicio 5
# Crea una función "contar_pares_impares" que reciba por parámetro:
# - lista: una lista de números enteros
# La función debe devolver 2 enteros (una tupla). El primer entero indica
# la cantidad de números pares y el segundo entero indica la cantidad de números
# impares de la lista recibida por parámetro.
def contar_pares_impares(lista):
    pares, impares = 0, 0
    for i in lista:
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
    return (f"Hay {pares} pares y {impares} impares")
print(contar_pares_impares(numeros))