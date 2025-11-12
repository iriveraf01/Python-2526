# Ejercicio 2
# Crea una función que muestre y sume los elementos de una lista que se encuentran en
# un índice determinado según la serie 1,4,7...(o sea, sumando 3 al anterior índice,
# comenzando en 1).
lista = [3, 13, 9, 49, 14, 10, 38, 11, 0, 34, 26, 34, 20, 9, 24, 42, 33, 35, 32, 14, 20, 24, 5]
# Salida debe ser así:
#  Lista[1]: 13
#  Lista[4]: 14
#  Lista[7]: 11
#  Lista[10]: 26
#  Lista[13]: 9
#  Lista[16]: 33
#  Lista[19]: 14
#  Lista[22]: 5
#  Suma total: 125
def ej2(lista):
    suma_total = 0
    for i in range(1, len(lista), 3):
        print(f"Lista[{i}]: {lista[i]}")
        suma_total += lista[i]
    print(f"Suma total: {suma_total}")
ej2(lista)