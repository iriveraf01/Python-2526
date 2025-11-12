# Ejercicio 3
# Crear una función que reciba como parámetro una lista.
# La función recorre la lista en orden inverso y suma los 5 últimos números que sean
# múltiplos de 3.
# reversed(lista) invierte una lista o usa slicing.
# Si no existen 5 números múltiplos de 3, informar de este hecho.
# Por último, mostrar la suma por pantalla.
# El 0 se considera múltiplo de todos los números.
lista = [3, 13, 9, 49, 14, 10, 38, 11, 0, 34, 26, 34, 20, 9, 24, 42, 33, 35, 32, 14, 20, 24, 5]
lista2 = [3, 13, 9, 49, 14, 10, 38, 11, 0, 34, 26, 34, 20, 42, 33, 35, 32, 14, 20, 24, 5]

def ej3(lista):
    hay_multiplos_de_3 = False
    contador_multiplos = 0
    suma_multiplos = 0
    for i in reversed(lista):
        if i % 3 == 0:
            contador_multiplos += 1
            suma_multiplos += i
            print(f"Número múltiplo de 3 encontrado: {i}")
        
        if contador_multiplos == 5:
            hay_multiplos_de_3 = True
            break
    
    if hay_multiplos_de_3 == False:
        print("No existen 5 números múltiplos de 3.")
    else:
        print(f"Suma de los últimos 5 múltiplos de 3: {suma_multiplos}")
ej3(lista)
ej3(lista2)
# Ejemplos:
# Lista1:
# Número múltiplo de 3 encontrado: 24
# Número múltiplo de 3 encontrado: 33
# Número múltiplo de 3 encontrado: 42
# Número múltiplo de 3 encontrado: 24
# Número múltiplo de 3 encontrado: 9
# Suma de los últimos 5 múltiplos de 3: 132
# Lista2:
# Número múltiplo de 3 encontrado: 24
# Número múltiplo de 3 encontrado: 33
# Número múltiplo de 3 encontrado: 42
# Número múltiplo de 3 encontrado: 0
# Número múltiplo de 3 encontrado: 9
# Suma de los últimos 5 múltiplos de 3: 108