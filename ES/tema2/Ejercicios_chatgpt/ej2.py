# a)
#   Crea un diccionario llamado lista_precios usando zip() donde:
#       Cada producto sea una clave
#       El valor sea un conjunto con todos sus precios
# b)
#   Elimina del diccionario todos los productos que tengan más de dos precios distintos.
# c)
#   Crea una tupla llamada resumen que contenga, para cada producto restante:
#       El nombre del producto
#       El precio mínimo
#       El precio máximo
#       Cada elemento de resumen debe ser una tupla.
# d)
#   Ordena la tupla resumen alfabéticamente por nombre de producto.
productos = ("pan", "leche", "huevos", "pan", "leche", "pan")
precios = (1.2, 0.9, 2.5, 1.3, 1.0, 1.1)

lista_precios = {}
for producto, precio in zip(productos, precios):
    if producto not in lista_precios:
        lista_precios[producto] = set()
    lista_precios[producto].add(precio)
print(lista_precios)

eliminar = {producto for producto, precio in lista_precios.items() if len(precio) > 2}
for i in eliminar:
    print(f"Se ha eliminado {i} que tiene {lista_precios.pop(i)}.")
print(lista_precios)

resumen = ()
for c,v in lista_precios.items():
    resumen += ((c, max(v), min(v)),)
print(resumen)

resumen = tuple(sorted(resumen))
print(resumen)