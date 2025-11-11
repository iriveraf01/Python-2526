# 4. Modificar la clase “Producto” del ejercicio anterior añadiendo un método que actualice
# la cantidad de un producto sumándole un valor pasado como parámetro. Mostrar los
# datos de un producto antes y después de ser modificada su cantidad.
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

producto1 = Producto("Camiseta", "Ropa", 15.99, 50)
producto1.actualizar_cantidad(22)
print(producto1)

productos = [Producto("tomate", "fruta", 2.3, 100), Producto("patata", "verdura", 1.5, 200), 
            Producto("cebolla", "verdura", 1.8, 150), Producto("manzana", "fruta", 3.2, 50),
            Producto("pera", "fruta", 2.7, 75)]

# 5. Visualizar en pantalla aquellos productos que pertenezcan a la categoría ‘verdura’.
for producto in productos:
    if producto.categoria == "verdura":
        print(producto)
# 6. Visualizar en pantalla aquellos productos cuyo precio esté entre 1.5 y 2.5 (incluidos).
for producto in productos:
    if producto.precio >= 1.5 and producto.precio <= 2.5:
        print(producto)
# 7. Obtener la media de los precios de los productos de la categoría ‘verdura’.
suma_precios = 0 
contador = 0
for producto in productos:
    if producto.categoria == "verdura":
        suma_precios += producto.precio
        contador += 1
media = suma_precios / contador
print(f"La media de los precios de las verduras es: {media}")
# 8. Contar cuántos productos tienen un precio entre 2 y 3 (excluidos).
contador = 0
for producto in productos:
    if producto.precio > 2 and producto.precio < 3:
        contador += 1
print(f"Hay {contador} de productos con un precio entre 2 y 3.")
# 9. Calcular la media de todos los precios de los productos.
# suma_precios = 0 
# contador = 0
for producto in productos:
    suma_precios += producto.precio
    contador += 1
media = suma_precios / contador
print(f"La media de los precios es: {media}")