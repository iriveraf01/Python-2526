# 1. Diseñar una clase llamada “Vehículo” con los atributos marca, modelo, año y precio.
# Crear dos objetos pertenecientes a esa clase e imprimir en pantalla la marca, el
# modelo y el precio de cada vehículo (mediante __str__). 
class Vehiculo:
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio
    
    def __str__(self):
        return f"Marca: {self.marca}. Modelo: {self.modelo}. Precio: {self.precio}"
    
coche = Vehiculo("BMW", "525d", 2002, "5.000€")
print(coche)
