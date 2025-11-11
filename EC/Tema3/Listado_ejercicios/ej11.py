# 11. Diseñar la clase “Empleado” con los atributos identificador, nombre, departamento,
# salario. Tener en cuenta que el salario será privado. Define un método para obtenerlo
# y otro para modificarlo.
# Programa el método __eq__(), de forma que indique si dos empleados son iguales o
# no en función de su salario.
# Crear varios empleados, mostrar sus datos y comparar si son iguales o no.
class Empleado:
    def __init__(self, identificador, nombre, departamento, salario):
        self.identificador = identificador
        self.nombre = nombre
        self.departamento = departamento
        self.salario = salario
    
    @property
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self, valor):
        if valor < 0:
            raise ValueError("El salario es menor a 0.")
        self.__salario = valor

    def __eq__(self, otro):
        if isinstance(otro, Empleado):
            return self.salario == otro.salario
        return False
    
emp1 = Empleado(1, "Juan", "Ventas", 2500)
emp2 = Empleado(2, "Ana", "Marketing", 3000)
emp3 = Empleado(1, "Juan", "Ventas", 2500)
print(emp1 == emp2)
print(emp1 == emp3)