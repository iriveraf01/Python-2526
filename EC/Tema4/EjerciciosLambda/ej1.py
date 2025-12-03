# Ejercicio 1
# Se te da una lista de diccionarios, donde cada diccionario representa un registro de un
# producto.
productos = [
    {'nombre': 'Laptop', 'precio': 1200, 'stock': 5},
    {'nombre': 'Mouse', 'precio': 25, 'stock': 12},
    {'nombre': 'Monitor', 'precio': 350, 'stock': 2},
    {'nombre': 'Teclado', 'precio': 75, 'stock': 8}
]
# Ordena la lista original de productos por precio de forma ascendente usando sorted() y
# una función lambda(). La salida es la siguiente:
# Salida: 
# Mouse: 25€
# Teclado: 75€
# Monitor: 350€
# Laptop: 1200€
ordenar_lista = sorted(productos, key=lambda producto: producto['precio'])
for i in ordenar_lista:
    print(f"{i['nombre']}: {i['precio']}€")