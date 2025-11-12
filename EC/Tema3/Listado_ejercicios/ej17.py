# 17. Debemos diseñar una aplicación Python que permita gestionar una lista de vehículos.
# a. Cada vehículo tiene como atributos: matrícula, marca, modelo, color, año,
# kilómetros, potencia y una lista de fechas en las que ha sido reparado.
# b. Dos vehículos se consideran iguales si tienen la misma matrícula.
# c. El constructor no recibe la lista de fechas como parámetro, sino que existe un
# método llamado agregar_reparación que añade una fecha a la lista.
# Los métodos asociados a la lista de vehículos son:
# - Añadir vehículo. No pueden existir varios vehículos con idéntica matrícula.
# - Retornar el número de reparaciones de un vehículo, a partir de su matrícula.
# - Eliminar un vehículo de la lista conociendo su matrícula.
# - Ordenar la lista de vehículos por año de compra.
# - Añadir reparación a un vehículo. Recibe matrícula y fecha de reparación.
# - Mostrar todos los vehículos.
class Vehiculo:
    def __init__(self, matricula, marca, modelo, color, año, kilometros, potencia):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.año = año
        self.kilometros = kilometros
        self.potencia = potencia
        self.fechas_reparacion = []
    
    def agregar_reparacion(self, fecha):
        self.fechas_reparacion.append(fecha)
    
    def __eq__(self, otro):
        if isinstance(otro, Vehiculo):
            return self.matricula == otro.matricula
        return False
    
    def __str__(self):
        return f"Matrícula: {self.matricula}, Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Reparaciones: {len(self.fechas_reparacion)}"  

class GestionVehiculo:
    lista_vehiculos = [
        Vehiculo("ABC123", "Toyota", "Corolla", "Rojo", 2019, 20000, 150),
        Vehiculo("DEF456", "Nissan", "Sentra", "Azul", 2018, 18000, 140),
        Vehiculo("GHI789", "Chevrolet", "Spark", "Blanco", 2017, 160400, 130),
        Vehiculo("JKL012", "Mazda", "3", "Negro", 2016, 15000, 120),
        Vehiculo("KKL122", "Volkswagen", "Golf", "Blanco", 2020, 230400, 120),
        Vehiculo("MMG122", "Nissan", "Micra", "Azul", 2020, 123000, 86),
        Vehiculo("ZZE123", "Seat", "Ibiza", "Blanco", 2010, 67000, 120),
    ]

    @classmethod
    def añadir_vehiculo(cls, vehiculo):
        if vehiculo not in cls.lista_vehiculos:
            cls.lista_vehiculos.append(vehiculo)
            return True
        return False
    
    @classmethod
    def numero_reparaciones(cls, matricula):
        for vehiculo in cls.lista_vehiculos:
            if vehiculo.matricula == matricula:
                return len(vehiculo.fechas_reparacion)
        return 0
    
    @classmethod
    def eliminar_vehiculo(cls, matricula):
        for vehiculo in cls.lista_vehiculos:
            if vehiculo.matricula == matricula:
                cls.lista_vehiculos.remove(vehiculo)
                return True
        return False
    
    @classmethod
    def ordenar_por_año(cls):
        cls.lista_vehiculos.sort(key=lambda v: v.año)

    @classmethod
    def añadir_reparacion_a_vehiculo(cls, matricula, fecha):
        for vehiculo in cls.lista_vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.agregar_reparacion(fecha)
                return True
        return False
    
    @classmethod
    def mostrar_vehiculos(cls):
        for vehiculo in cls.lista_vehiculos:
            print(vehiculo)


GestionVehiculo.añadir_reparacion_a_vehiculo("ABC123", "2023-01-15")
GestionVehiculo.añadir_reparacion_a_vehiculo("ABC123", "2023-03-22")
print("Número de reparaciones del vehículo ABC123:", GestionVehiculo.numero_reparaciones("ABC123"))
GestionVehiculo.añadir_vehiculo(Vehiculo("NEW999", "Hyundai", "Elantra", "Gris", 2021, 10000, 160))
GestionVehiculo.eliminar_vehiculo("GHI789")
GestionVehiculo.ordenar_por_año()
GestionVehiculo.mostrar_vehiculos()
