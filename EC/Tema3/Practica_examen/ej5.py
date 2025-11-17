# Ejercicio 5
# Crea una función que reciba dos listas, lista pares y lista impares.
# La función multiplica ambas listas elemento a elemento, guardando el resultado
# en una nueva lista. Al final retorna la lista “resultado”.
# Es decir, resultado[i]=pares[i] * impares[i].
# Hay que tener en cuenta que ambas listas pueden ser de diferente tamaño.
# Por ejemplo:
# pares = [2, 4, 8]
# impares = [3]
# El resultado se rellena con los restos de los elementos de la lista mayor, es decir,
# resultado = [6, 4, 8]
# Requisitos:
# - Debes tener en cuenta todos los casos posibles en cuanto a tamaños de listas
# recibidas.
# - Si no es un entero debido a que un operando es una letra (por ejemplo al multiplicar
# 'b' * 4 el resultado es 'bbbb').
def multiplicar_listas(pares, impares):
    resultado = []
    len_pares = len(pares)
    len_impares = len(impares)
    min_len = min(len_pares, len_impares)

    # Multiplicar los elementos comunes
    for i in range(min_len):
        resultado.append(pares[i] * impares[i])

    # Añadir los elementos restantes de la lista mayor
    if len_pares > len_impares:
        resultado.extend(pares[min_len:])
    else:
        resultado.extend(impares[min_len:])

    return resultado
# Ejemplos de uso
pares1 = [2, 4, 8]
impares1 = [3]
print(multiplicar_listas(pares1, impares1))  # Salida: [6, 4, 8]