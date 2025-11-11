# 13. Para este ejercicio utilizaremos la lista de productos vista antes. Accederemos al
# primer objeto de la lista y le añadiremos el atributo caducado con el valor True.
# Recorremos la lista y visualizamos el atributo __dict__ de cada objeto. Recuerda que
# este atributo proporciona información sobre los atributos de un objeto, en forma de
# diccionario.
class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"Nombre: {self.nombre}. Categoria: {self.categoria}. Precio: {self.precio}. Cantidad: {self.cantidad}"

    def actualizar_cantidad(self, valor):
        self.cantidad += valor

productos = [Producto("tomate", "fruta", 2.3, 100), Producto("patata", "verdura", 1.5, 200), 
            Producto("cebolla", "verdura", 1.8, 150), Producto("manzana", "fruta", 3.2, 50),
            Producto("pera", "fruta", 2.7, 75)]

productos[0].caducado = True
for producto in productos:
    print(producto.__dict__)