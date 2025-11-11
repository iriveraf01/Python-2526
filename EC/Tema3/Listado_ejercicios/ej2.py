# 2. En este ejercicio utilizaremos la misma clase que en el ejercicio anterior y añadiremos
# un método llamado “nombre_completo” que retorne en una cadena los atributos marca
# y modelo concatenados y separados por un guión (Seat-Ibiza). Crear dos objetos y
# probar el método. 

class Vehiculo:
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio
    
    def nombre_completo(self):
        return f"({self.marca}-{self.modelo})"
    
    def __str__(self):
        return f"Marca: {self.marca}. Modelo: {self.modelo}. Precio: {self.precio}"
    
coche = Vehiculo("BMW", "525d", 2002, "5.000€")
print(coche.nombre_completo())
