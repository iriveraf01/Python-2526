# Ejercicios conjuntos
# Ejercicio 1
# Dada una lista de números, elimina los duplicados y ordénala.
# numeros = [3, 5, 3, 2, 2, 9, 1]
# numeros = [3, 5, 3, 2, 2, 9, 1]
# numeros = list(set(numeros))
# print(sorted(numeros))

# Ejercicio 2
# Comprueba si un usuario tiene los permisos mínimos requeridos.
# usuario = {"read", "write"}
# requeridos = {"read"}
# usuario = {"read", "write"}
# requeridos = {"read"}
# print(usuario.issuperset(requeridos))

# Ejercicio 3
# Muestra qué productos hay en una tienda, pero no en la otra.
# tienda1 = {"raton", "teclado", "monitor"}
# tienda2 = {"monitor", "altavoces"}
# tienda1 = {"raton", "teclado", "monitor"}
# tienda2 = {"monitor", "altavoces"}
# print(f"En la tienda1 hay {tienda1 - tienda2} mientras que en la tienda2 hay {tienda2 - tienda1}")

# Ejercicio 4 – Contador de palabras
# Crea una función llamada contar_palabras que reciba un texto y cuente la frecuencia de
# cada palabra en el texto. Debes eliminar primero los signos de puntuación.
# La función Retorna un diccionario que almacena las palabras como claves y su
# frecuencia como valores.
# Una vez obtienes el resultado, muestra la frecuencia de cada palabra recorriendo el
# diccionario con un for.
# def contar_palabras(cadena):
#     cadena = cadena.replace(",", "").replace(".", "").lower()
#     palabras = cadena.split()
#     frecuencia = {}

#     for palabra in palabras:
#         if palabra in frecuencia:
#             frecuencia[palabra] += 1
#         else:
#             frecuencia[palabra] = 1
#     return frecuencia

# cadena = "Hola adios hola, cola, adios, parchis"
# resultado = contar_palabras(cadena)
# for palabra, freq in resultado.items():
#     print(f"La palabra '{palabra}' aparece {freq} veces.")


# Ejercicio 5 – Lotería.
# Crea una función llamada "premios" para simular un sorteo de lotería de 2 cifras. Se
# harán 20 tiradas. Se debe utilizar el módulo random para generar las tiradas. Cada tirada
# es un número, todas las tiradas se almacenan en un conjunto y se retornan. No puede
# haber 2 números iguales, es decir, si ya ha salido el 54, no puede volver a salir...
# Crea otra función llamada "apuesta" con 5 tiradas aleatorias. Estas serán los números
# que juega el jugador.
# Crea otra función llamada "comprobación" que compara ambos conjuntos para saber
# cuántos números ha acertado. Debes hacer la comprobación mediante operaciones de
# conjuntos. Debes retornar una tupla con la cantidad de números acertados y la cantidad
# de números no acertados, es decir (acertados, no_acertados).

import random

def premios():
    
    return None

def apuesta():
    num_aleatorio = random.randint(1, 10)
    return num_aleatorio

def comprobacion():
    return None


# Ejercicio 6 – Agenda telefónica
# Implementa una agenda telefónica simple utilizando un diccionario. Las claves serán los
# nombres y los valores serán tuplas con el número de teléfono y la dirección.
# Debes crear las siguientes funciones:
# - Introducir un nuevo contacto
# - Buscar un contacto por nombre y mostrar su teléfono y dirección.
# - Eliminar contacto por nombre
# - Mostrar toda la agenda
# - Eliminar toda la agenda



# Ejercicio 7 – Poker
# Vamos a representar una mano de poker utilizando una tupla de cinco elementos, donde
# cada elemento es una tupla (valor, palo).
# Por ejemplo: (('9', 'picas'), ('3', 'corazones'), ('8', 'diamantes'), ('9', 'tréboles'), ('5',
# 'tréboles'))
# La función proporcionada genera una mano aleatoria.
# Debes implementar varias funciones para evaluar si tiene poker, escalera de color,
# escalera o color. Estas funciones retornan true/false si cumple los criterios. Es decir, si
# la mano recibida como parámetro es poker, la función "es_poker" retorna True.
# Una vez tengas las funciones por separado, crea una nueva función que reciba la mano y
# devuelva la combinación de mejor puntuación en forma de string, es decir, retorna uno
# de estos valores:
# - 'poker'
# - 'escalera color'
# - 'escalera'
# - 'color'
# - none Si no tiene ninguna combinación válida.


