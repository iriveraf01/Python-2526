# Ejercicio 4
# Crea la función "generar_listas()". Esta función lee de teclado una serie de números
# enteros hasta que se introduzca el 0. La función guarda los números introducidos
# (enteros) en 2 listas, lista pares y lista impares.
# La función retorna ambas listas(tupla).
# Requisitos:
# + Utilizar una expresión IF
# + Hacer control de excepciones sobre el elemento introducido en teclado. Solamente
# pueden ser números enteros.
# Si se introduce algo que no es entero, mostrar "El valor ingresado no es un número
# entero" y seguir pidiendo números.
# El control de excepciones debe ser el justo para que controle la introducción de
# enteros, sin necesidad de probar cosas adicionales o innecesarias, utilizando la/s
# excepciones específicas, no la genérica.
def generar_listas():
    numero = 1
    while numero != 0:
        return