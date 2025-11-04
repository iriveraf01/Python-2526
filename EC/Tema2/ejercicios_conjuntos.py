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
# for palabra, veces in resultado.items():
#     print(f"La palabra '{palabra}' aparece {veces} veces.")


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
    tiradas = set()
    # Genero tiradas hasta tener 20 números únicos
    while len(tiradas) < 20:
        tirada = random.randint(0, 99)
        # Añado la tirada al conjunto (si ya existe, no se añade)
        tiradas.add(tirada)
    return tiradas

def apuesta():
    jugada = set()
    # Genero jugada hasta tener 5 números únicos
    while len(jugada) < 5:
        numero = random.randint(0, 99)
        # Añado el número al conjunto (si ya existe, no se añade)
        jugada.add(numero)
    return jugada

def comprobacion(tiradas, jugada):
    # Intersection significa números que están en ambos conjuntos
    acertados = tiradas.intersection(jugada)
    # El menos significa números que están en jugada pero no en tiradas
    no_acertados = jugada - tiradas
    return (len(acertados), len(no_acertados))

tiradas = premios()
jugada = apuesta()
resultado = comprobacion(tiradas, jugada)
print(f"Tiradas de la lotería: {tiradas}")
print(f"Números jugados: {jugada}")
print(f"Números acertados: {resultado[0]}, Números no acertados: {resultado[1]}")


# Ejercicio 6 – Agenda telefónica
# Implementa una agenda telefónica simple utilizando un diccionario. Las claves serán los
# nombres y los valores serán tuplas con el número de teléfono y la dirección.
# Debes crear las siguientes funciones:
# - Introducir un nuevo contacto
# - Buscar un contacto por nombre y mostrar su teléfono y dirección.
# - Eliminar contacto por nombre
# - Mostrar toda la agenda
# - Eliminar toda la agenda

# agenda = {}
# def introducir_contacto(nombre, telefono, direccion):
#     # Si el contacto ya existe, no lo añadimos
#     if nombre in agenda:
#         return "El contacto ya existe"
#     # Se añade el nombre como clave y una tupla (teléfono, dirección) como valor
#     agenda[nombre] = (telefono, direccion)
#     return "Contacto añadido"

# def buscar_contacto(nombre):
#     # Retorna el contacto si existe, sino un mensaje de no encontrado
#     return agenda.get(nombre, "Contacto no encontrado")

# def eliminar_contacto(nombre):
#     if nombre in agenda:
#         # Elimina el contacto por el nombre
#         del agenda[nombre]
#         return "Contacto eliminado"
#     else:
#         return "Contacto no encontrado"
    
# def mostrar_agenda():
#     return agenda

# def eliminar_agenda():
#     agenda.clear()

# print(introducir_contacto("Juan", "123456789", "Calle Falsa 123"))
# print(introducir_contacto("Ana", "987654321", "Avenida Siempre Viva 456"))
# print(buscar_contacto("Juan"))
# print(buscar_contacto("Pedro"))
# print(mostrar_agenda())
# print(eliminar_contacto("Ana"))
# print(mostrar_agenda())


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

# import random

# def generar_mano():
#     valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
#     palos = ['picas', 'corazones', 'diamantes', 'tréboles']
#     mano = set()
#     while len(mano) < 5:
#         # Choice selecciona un elemento aleatorio de la lista
#         valor = random.choice(valores)
#         palo = random.choice(palos)
#         mano.add((valor, palo))
#     return tuple(mano)

# def es_poker(mano):
#     # valores = a los valores de las cartas en la mano [10, 'J', '3', '10', '10']
#     # carta[0] es el valor de la carta
#     valores = [carta[0] for carta in mano]
#     # Recorro los valores y contamos cuántas veces aparece cada uno
#     for valor in set(valores):
#         # Si algún valor aparece 4 veces, es poker
#         if valores.count(valor) == 4:
#             return True
#     return False

# def es_color(mano):
#     # palos = a los palos de las cartas en la mano ['picas', 'corazones', 'picas', 'picas', 'picas']
#     # carta[1] es el palo de la carta
#     palos = [carta[1] for carta in mano]
#     # Retorna True si todos los palos son iguales
#     # len(set(palos)) cuenta cuántos palos diferentes hay sin repetidos
#     return len(set(palos)) == 1

# def es_escalera(mano):
#     valores_ordenados = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
#     # valores_mano = índices de los valores de las cartas en la mano según su orden
#     # carta[0] es el valor de la carta
#     # Básicamente convierte los valores de las cartas en sus índices correspondientes
#     valores_mano = sorted([valores_ordenados.index(carta[0]) for carta in mano])
#     # Retorna True si los valores son consecutivos
#     # all() es porque debe cumplirse para todos los elementos
#     return all(valores_mano[i] + 1 == valores_mano[i + 1] for i in range(len(valores_mano) - 1))

# def evaluar_mano(mano):
#     if es_poker(mano):
#         return 'poker'
#     elif es_color(mano) and es_escalera(mano):
#         return 'escalera color'
#     elif es_escalera(mano):
#         return 'escalera'
#     elif es_color(mano):
#         return 'color'
#     else:
#         return 'No tiene combinación válida'
# mano = generar_mano()
# print(f"Mano generada: {mano}")
# resultado = evaluar_mano(mano) 
# print(f"Resultado de la mano: {resultado}")