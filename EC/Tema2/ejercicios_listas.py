# Ejercicios listas
# Ejercicio 1
# El mensaje secreto. Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje
# "secreto"
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# secreto = mensaje[7:]
# print("".join(secreto))

# Ejercicio 2
# Intercambio de posiciones. Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.
# numeros = [10, 20, 30, 40, 50]
# aux = numeros[0]
# numeros[0] = numeros[-1]
# numeros[-1] = aux
# print(numeros)

# Ejercicio 3
# El sándwich de listas. Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan
# de abajo, en ese orden.
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# sandwich = pan , ingredientes, pan_abajo
# print(sandwich)

# Ejercicio 4
# Duplicando la lista. Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
# lista = [1, 2, 3]
# duplicada = lista * 2
# print(duplicada)

# Ejercicio 5
# Extrayendo el centro. Dada una lista con un número impar de elementos, extrae el
# elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30
# lista = [10, 20, 30, 40, 50]
# centro = len(lista) // 2
# print(lista[centro])

# Ejercicio 6
# Reversa parcial. Dada una lista, invierte solo la primera mitad de la lista (utilizando
# slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
# lista = [1, 2, 3, 4, 5, 6]
# mitad = len(lista) // 2
# lista_ordenada = lista[:-mitad]
# lista_ordenada.sort(reverse=True)
# lista_ordenada.extend(lista[mitad:])
# print(lista_ordenada)

# Ejercicios métodos de listas
# Ejercicio 1
# Añadir y modificar elementos. Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.
# lista = [1, 2, 3, 4, 5]
# lista.append(6)
# lista.insert(2, 10)
# lista[0] = 0
# print(lista)

# Ejercicio 2
# Combinar y limpiar listas. Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento
# eliminado.
# Limpia completamente lista_b usando clear().
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# lista_a.extend(lista_b)
# lista_a.remove(1)
# print(lista_a.pop(3))
# lista_b.clear()
# print(lista_a)
# print(lista_b)

# Ejercicio 3
# Slicing y eliminación con “del”.
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir
# el 5).
# Imprime la lista resultante.

# lista = []
# lista.extend(range(1, 21))
# print(lista)
# del(lista[1:4])
# print(lista)

# Ejercicio 4
# Ordenar y contar. Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.
# numeros = [5, 2, 8, 1, 9, 4, 2]
# numeros.sort()
# print(numeros)
# print(numeros.count(2))
# print(7 in numeros)

# Ejercicio 5
# Copia vs. Referencia. Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.
# numeros = [1, 2, 3]
# copia_1 = numeros[:]
# copia_2 = numeros.copy()
# referencia = numeros
# referencia[0] = 10
# print(numeros)
# print(copia_1)
# print(copia_2)
# print(referencia)

# Ejercicio 6
# Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
cadenas = ["Manzana", "pera", "BANANA", "naranja"]
cadenas.sort()
print(cadenas)