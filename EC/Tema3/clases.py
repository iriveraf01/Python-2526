# Ejercicio 1
# Crea una clase Persona con los atributos nombre y edad. Debe tener un método
# presentarse() que imprima algo como: “Hola, me llamo Ana y tengo 25 años.”

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

mi_colega = Persona("Pabel", 22)

mi_colega.presentarse()