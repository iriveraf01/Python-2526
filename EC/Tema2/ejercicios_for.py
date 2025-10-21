# Ejercicios FOR
# Ejercicio 1
# Imprimir números pares. Imprime todos los números pares del 2 al 20 (inclusive)
# usando un bucle for.
for i in range(2, 21, 2):
    print(i, end=" ")

# Ejercicio 2
# Calcular la media de una lista. Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]. Calcula la media de los números usando un bucle for.
numeros = [10, 20, 30, 40, 50]
suma = 0
for numero in numeros:
    suma += numero
media = suma / len(numeros)
print("\nLa media es:", media)

# Ejercicio 3
# Buscar el máximo de una lista. Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
numeros = [15, 5, 25, 10, 20]
maximo = numeros[0]
for numero in numeros:
    if numero > maximo:
        maximo = numero
print("El número máximo es:", maximo)

# Ejercicio 4
# Filtrar cadenas por longitud. Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras usando un bucle
# for y list comprehension.
palabras = ["casa", "arbol", "sol", "elefante", "luna"]
nuevas_palabras = [palabra for palabra in palabras if len(palabra) >= 5]
print(nuevas_palabras)


# Ejercicio 5
# Contar palabras que empiezan con una letra. Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra. Cuenta cuántas palabras en la lista empiezan
# con esa letra (sin diferenciar mayúsculas/minúsculas).
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra = input("Introduce una letra: ").lower()
contador = 0
for palabra in palabras:
    if palabra.lower().startswith(letra):
        contador += 1
print(f"Número de palabras que empiezan con '{letra}':", contador)