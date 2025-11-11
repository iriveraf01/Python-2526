# 3. Diseñar una clase Python llamada “Producto” con los atributos nombre, categoría,
# precio y cantidad. Diseña en esta clase el método __str__ de forma que retorne todos
# los atributos en un dato de tipo cadena (str).
# Crear dos productos pertenecientes a esa clase y mostrar todos los datos de aquel
# producto que tenga mayor precio.
class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"Nombre: {self.nombre}. Categoria: {self.categoria}. Precio: {self.precio}. Cantidad: {self.cantidad}"

producto1 = Producto("Camiseta", "Ropa", 15.99, 50)
producto2 = Producto("Pantalon", "Ropa", 25.99, 30)
if producto1.precio > producto2.precio:
    print(producto1)
else:
    print(producto2)
