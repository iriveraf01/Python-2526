# 1. Diseñar una clase llamada “Vehículo” con los atributos marca, modelo, año y precio.
# Crear dos objetos pertenecientes a esa clase e imprimir en pantalla la marca, el
# modelo y el precio de cada vehículo (mediante __str__). 
# class Vehiculo:
#     def __init__(self, marca, modelo, año, precio):
#         self.marca = marca
#         self.modelo = modelo
#         self.año = año
#         self.precio = precio
    
#     def __str__(self):
#         return f"Marca: {self.marca}. Modelo: {self.modelo}. Precio: {self.precio}"
    
# coche = Vehiculo("BMW", "525d", 2002, "5.000€")
# print(coche)

# 2. En este ejercicio utilizaremos la misma clase que en el ejercicio anterior y añadiremos
# un método llamado “nombre_completo” que retorne en una cadena los atributos marca
# y modelo concatenados y separados por un guión (Seat-Ibiza). Crear dos objetos y
# probar el método. 

# class Vehiculo:
#     def __init__(self, marca, modelo, año, precio):
#         self.marca = marca
#         self.modelo = modelo
#         self.año = año
#         self.precio = precio
    
#     def nombre_completo(self):
#         return f"({self.marca}-{self.modelo})"
    
#     def __str__(self):
#         return f"Marca: {self.marca}. Modelo: {self.modelo}. Precio: {self.precio}"
    
# coche = Vehiculo("BMW", "525d", 2002, "5.000€")
# print(coche.nombre_completo())

# 3. Diseñar una clase Python llamada “Producto” con los atributos nombre, categoría,
# precio y cantidad. Diseña en esta clase el método __str__ de forma que retorne todos
# los atributos en un dato de tipo cadena (str).
# Crear dos productos pertenecientes a esa clase y mostrar todos los datos de aquel
# producto que tenga mayor precio.
# class Producto:
#     def __init__(self, nombre, categoria, precio, cantidad):
#         self.nombre = nombre
#         self.categoria = categoria
#         self.precio = precio
#         self.cantidad = cantidad

#     def __str__(self):
#         return f"Nombre: {self.nombre}. Categoria: {self.categoria}. Precio: {self.precio}. Cantidad: {self.cantidad}"

# producto1 = Producto("Camiseta", "Ropa", 15.99, 50)
# producto2 = Producto("Pantalon", "Ropa", 25.99, 30)
# if producto1.precio > producto2.precio:
#     print(producto1)
# else:
#     print(producto2)

# 4. Modificar la clase “Producto” del ejercicio anterior añadiendo un método que actualice
# la cantidad de un producto sumándole un valor pasado como parámetro. Mostrar los
# datos de un producto antes y después de ser modificada su cantidad.
# class Producto:
#     def __init__(self, nombre, categoria, precio, cantidad):
#         self.nombre = nombre
#         self.categoria = categoria
#         self.precio = precio
#         self.cantidad = cantidad

#     def __str__(self):
#         return f"Nombre: {self.nombre}. Categoria: {self.categoria}. Precio: {self.precio}. Cantidad: {self.cantidad}"

#     def actualizar_cantidad(self, valor):
#         self.cantidad += valor

# producto1 = Producto("Camiseta", "Ropa", 15.99, 50)
# producto1.actualizar_cantidad(22)
# print(producto1)

# productos = [Producto("tomate", "fruta", 2.3, 100), Producto("patata", "verdura", 1.5, 200), 
#             Producto("cebolla", "verdura", 1.8, 150), Producto("manzana", "fruta", 3.2, 50),
#             Producto("pera", "fruta", 2.7, 75)]

# 5. Visualizar en pantalla aquellos productos que pertenezcan a la categoría ‘verdura’.
# for producto in productos:
#     if producto.categoria == "verdura":
#         print(producto)
# 6. Visualizar en pantalla aquellos productos cuyo precio esté entre 1.5 y 2.5 (incluidos).
# for producto in productos:
#     if producto.precio >= 1.5 and producto.precio <= 2.5:
#         print(producto)
# 7. Obtener la media de los precios de los productos de la categoría ‘verdura’.
# suma_precios = 0 
# contador = 0
# for producto in productos:
#     if producto.categoria == "verdura":
#         suma_precios += producto.precio
#         contador += 1
# media = suma_precios / contador
# print(f"La media de los precios de las verduras es: {media}")
# 8. Contar cuántos productos tienen un precio entre 2 y 3 (excluidos).
# contador = 0
# for producto in productos:
#     if producto.precio > 2 and producto.precio < 3:
#         contador += 1
# print(f"Hay {contador} de productos con un precio entre 2 y 3.")
# 9. Calcular la media de todos los precios de los productos.
# suma_precios = 0 
# contador = 0
# for producto in productos:
#     suma_precios += producto.precio
#     contador += 1
# media = suma_precios / contador
# print(f"La media de los precios es: {media}")

# 10. Diseñar una clase llamada “Mates” con los métodos estáticos que se describen:
# a. mayor. Recibe dos números como argumento y retorna el mayor.
# b. producto. Recibe tres números como argumento y retorna su producto.
# c. potencia. Recibe una base y un exponente como argumentos y retorna la base
# elevada al exponente.
# Probar los métodos programados.
# class Mates:
#     @staticmethod
#     def mayor(numero1, numero2):
#         return numero1 if numero1 > numero2 else numero2
    
#     @staticmethod
#     def producto(numero1, numero2, numero3):
#         return numero1 * numero2 * numero3
    
#     @staticmethod
#     def potencia(base, exponente):
#         return base ** exponente
# print(Mates.mayor(5, 10))
# print(Mates.producto(2, 3, 4))
# print(Mates.potencia(2, 3))

# 11. Diseñar la clase “Empleado” con los atributos identificador, nombre, departamento,
# salario. Tener en cuenta que el salario será privado. Define un método para obtenerlo
# y otro para modificarlo.
# Programa el método __eq__(), de forma que indique si dos empleados son iguales o
# no en función de su salario.
# Crear varios empleados, mostrar sus datos y comparar si son iguales o no.
# class Empleado:
#     def __init__(self, identificador, nombre, departamento, salario):
#         self.identificador = identificador
#         self.nombre = nombre
#         self.departamento = departamento
#         self.__salario = salario
    
#     @property
#     def salario(self):
#         return self.__salario
#     @salario.setter
#     def salario(self, valor):
#         if valor < 0:
#             raise ValueError("El salario es menor a 0.")
#         self.__salario = valor

#     def __eq__(self, otro):
#         if isinstance(otro, Empleado):
#             return self.identificador == otro.identificador and self.nombre == otro.nombre and self.departamento == otro.departamento
#         return False
    
# emp1 = Empleado(1, "Juan", "Ventas", 2500)
# emp2 = Empleado(2, "Ana", "Marketing", 3000)
# emp3 = Empleado(1, "Juan", "Ventas", 2500)
# print(emp1 == emp2)
# print(emp1 == emp3)

# 12. Diseñar una aplicación Python que trabaje con objetos de la clase “Partido”. Cada
# partido tendrá como atributos equipo local, equipo visitante, goles local, goles
# visitante, campeonato y fecha.
# La aplicación consta también de una clase llamada “GestionPartidos” que tendrá como
# atributo de clase una lista de partidos y los métodos siguientes:
#   - Filtrar por equipo local. Recibe un equipo local como argumento e imprime
#     todos los partidos de ese equipo actuando como local.
#   - Ganados del equipo. Recibe un equipo como argumento y retorna cuántos
#     partidos ganó ese equipo, independientemente de si actuó como local o como
#     visitante.
#   - Mostrar los partidos del año pasado como parámetro.
#   - Mostrar los partidos de una fecha pasada como parámetro.
#   - Añadir un nuevo partido a la lista de partidos.
#   - Cuenta partidos. Retorna el número de partidos de la lista.
# Prueba las clases y los métodos creados.

class Partido:
    def __init__(self, equipo_local, equipo_visitante, goles_local, goles_visitante, campeonato, fecha):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.goles_local = goles_local
        self.goles_visitante = goles_visitante
        self.campeonato = campeonato
        self.fecha = fecha

class GestionPartido:
    lista_partidos = []

    @classmethod
    def filtrar_equipo_local(cls, local):
        return True
