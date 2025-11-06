# Ejercicio 1
# Crea una clase Persona con los atributos nombre y edad. Debe tener un método
# presentarse() que imprima algo como: “Hola, me llamo Ana y tengo 25 años.”

# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad
    
#     def presentarse(self):
#         print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

# mi_colega = Persona("Pabel", 22)

# mi_colega.presentarse()

# Ejercicio 2
# Crea una clase Rectangulo con:
# • Un método de instancia area() que devuelva base × altura;
# • Un método de clase cuadrado(lado) que cree un cuadrado con base = altura.
# • Un método estático es_valido(base, altura) que devuelva True si ambos son
# positivos.

# class Rectangulo:
#     def __init__(self, base, altura, lado):
#         self.base = base
#         self.altura = altura
#         self.lado = lado

#     def area(self):
#         return self.base * self.altura
    
#     @classmethod
#     def cuadrado(cls, lado):
#         return cls(lado, lado)
        

#     @staticmethod
#     def es_valido(base, altura):
#         return True if base > 0 and altura > 0 else False

# mi_rectangulo = Rectangulo(4, 5, 6)
# print(mi_rectangulo.area())

# # cuadrado = Rectangulo.cuadrado(5)
# # print(cuadrado.area())

# print(Rectangulo.es_valido(4, 5))
# print(Rectangulo.es_valido(-4, 5))

# Ejercicio 3
# Crea una clase Rectangulo con atributos base y altura.
# Usa @property para:
# • Validar que ambos sean positivos.
# • Calcular el área como propiedad de solo lectura (area).

# class Rectangulo:

#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura

#     def area(self):
#         return self.base * self.altura
    
#     @property
#     def base(self):
#         return self._base
    
#     @base.setter
#     def base(self, valor):
#         if valor < 0:
#             raise ValueError("La base es negativa")
#         self._base = valor

#     @property
#     def altura(self):
#         return self._altura
    
#     @base.setter
#     def altura(self, valor):
#         if valor < 0:
#             raise ValueError("La altura es negativa")
#         self._altura = valor

# mi_rectangulo = Rectangulo(5, 5)
# print(mi_rectangulo.area())

# Ejercicio 4
# Crea una clase llamada Producto que represente un artículo en un inventario.
# Requisitos de la Clase:
# 1. Atributos de Instancia:
# o _nombre (string): Nombre del producto.
# o _precio (float): Precio de venta del producto.
# o _stock (int): Cantidad disponible en el inventario.
# 2. Atributo de Clase:
# o total_inventario (int): Debe llevar la cuenta total de unidades en stock
# de todos los productos.
# 3. Encapsulación y Validación (@property):
# o Implementa el getter y setter para precio. El setter debe asegurar que el
# precio sea siempre mayor que 0.0. Si se intenta asignar un precio no
# válido, debe lanzar una excepción ValueError: raise ValueError("El
# precio debe ser mayor que cero.")
# o Implementa el getter y setter para stock. El setter debe asegurar que el
# stock sea mayor o igual a 0. Además, cada vez que se modifique el stock,
# el atributo de clase total_inventario debe actualizarse.
# 4. Método de Clase:
# o @classmethod mostrar_total_inventario(): Un método que imprima el
# valor actual de total_inventario.
# 5. Método de Instancia:
# o vender(cantidad): Un método que descuente cantidad del stock actual si
# hay suficiente. Si no hay suficiente stock, debe lanzar una
# excepción ValueError.
# Mejora la representación del objeto para la salida usando __repr__, el precio con 2
# decimales

class Producto:

    total_inventario = 0

    def __init__(self, nombre:str, precio:float, stock:int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        Producto.total_inventario = stock

    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio es menor a 0.")
        self._precio = valor
    
    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, valor):
        if valor <= 0:
            raise ValueError("El stock es menor de 0.")
        self._stock = valor

    @classmethod
    def mostrar_total_inventario(cls):
        return print(f"El inventario total es de: {cls.total_inventario}")
    
    def vender(self, cantidad):
        self.stock -= cantidad
        return print(f"Se ha vendido {cantidad} del producto ({self.nombre}).")
    
    def __str__(self):
        return f"Producto(nombre={self.nombre}, precio={self.precio:.2f}, stock={self.stock})"

mi_producto = Producto("Camisa", 19.99, 50)
print(mi_producto)
Producto.mostrar_total_inventario()
mi_producto.vender(5)
print(mi_producto)