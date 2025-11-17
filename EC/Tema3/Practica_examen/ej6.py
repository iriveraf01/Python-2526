# Ejercicio 6
# Crea una función "extraer_elemento(lista)" que recibe por parámetro una lista.
# La función realiza:
# - Si la lista está vacía, indica que "La lista está vacía"
# - Si la lista tiene un elemento: mostrar el elemento con el mensaje "Solo hay 1
# elemento: x"
# - Si la lista tiene más de 1 elemento pero el primero es par, mostrar: "Primer elemento
# es par -> x"
# - Si la lista tiene más de 1 elemento pero el primero es impar, mostrar: "Primer
# elemento es impar-> x"
# La función retorna el resto de la lista no mostrada, o, si se produce una excepción,
# retorna None.
# Requisitos:
# - Utilizar estructura match con patrones sobre la lista.

def extraer_elemento(lista):
    try:
        match lista:
            case []:
                print("La lista está vacía")
                return []

            case [x]:
                print(f"Solo hay 1 elemento: {x}")
                return []

            case [x, *resto]:
                if x % 2 == 0:
                    print(f"Primer elemento es par -> {x}")
                else:
                    print(f"Primer elemento es impar -> {x}")
                return resto

    except Exception:
        return None


lista = [4, 3, 16, 5, 7, 8]
print(f"El resto devuelto es: {extraer_elemento(lista)}")