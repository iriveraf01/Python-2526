# Ejercicio 7
# Disponemos de 2 parámetros de entrada en la función:
# - palabra_objetivo: La palabra que hay que adivinar.
# - letras_introducidas: Lista de letras ya introducidas.
# La función es "dar_pista(palabra_objetivo, letras_introducidas)"
# La función busca la letra que se repite menos veces en "palabra_objetivo" y
# que aún no está en "letras_introducidas" y la retorna. Si hay varias letras que
# se repiten el mismo número mínimo de veces, elegir la primera de ellas.
# Se puede usar la función lista.count('letra') que cuenta las apariciones de 'letra'
# en la lista.
def dar_pista(palabra_objetivo, letras_introducidas):
    letra_elegida = None
    repeticiones_mas_bajas = None

    for letra in palabra_objetivo.lower():
        if letra not in letras_introducidas:

            repeticiones = palabra_objetivo.count(letra)

            if repeticiones_mas_bajas is None or repeticiones < repeticiones_mas_bajas:
                letra_elegida = letra
                repeticiones_mas_bajas = repeticiones

    return letra_elegida

palabra = "programacion"
usadas = ['a', 'o', 'r']

pista = dar_pista(palabra, usadas)

print("La pista es:", pista)