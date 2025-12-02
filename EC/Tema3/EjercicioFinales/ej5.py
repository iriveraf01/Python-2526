# Ejercicio 5 - Herencia y Sobrescritura (Tema: Gestión de vehículos sostenibles)
# Una empresa municipal gestiona dos tipos de vehículos: bicicletas eléctricas y patinetes
# eléctricos. Ambos comparten características comunes:
# • identificador
# • nivel de batería
# • método estado(). Devuelve una descripción del vehículo:
# [identificador] Batería: X%
# Se pide:
# 1. Crear una clase base VehiculoElectrico con los atributos y el método estado()
# mencionados.
# 2. Crear dos clases hijas:
# • BicicletaElectrica
# • PatineteElectrico
# 3. Cada clase hija debe sobrescribir el método estado() para incluir información
# adicional(puede que la subclase tenga nuevos atributos):
# • Bicicleta eléctrica → número de marchas
# • Patinete eléctrico → velocidad máxima
# Estado mostrará (Ojo que la primera parte es del padre):
# “[Identificador] Batería X% | Tipo: Patinete eléctrico | Vel. max: X km/h”
# “[Identificador] Batería X% | Tipo: Bicicleta eléctrica | Marchas: X”
class VehiculoElectrico:
    def __init__(self, identificador, nivel_bateria):
        self.identificador = identificador
        self.nivel_bateria = nivel_bateria
    
    def estado(self):
        return f"[{self.identificador}] Batería: {self.nivel_bateria}%"

class BicicletaElectrica(VehiculoElectrico):
    def __init__(self, identificador, nivel_bateria, numero_marchas):
        super().__init__(identificador, nivel_bateria)
        self.numero_marchas = numero_marchas
    
    def estado(self):
        padre = super().estado()
        return f"{padre} | Tipo: Bicicleta eléctrica | Marchas: {self.numero_marchas}"

class PatineteElectrico(VehiculoElectrico):
    def __init__(self, identificador, nivel_bateria, vel_max):
        super().__init__(identificador, nivel_bateria)
        self.vel_max = vel_max
    
    def estado(self):
        padre = super().estado()
        return f"{padre} | Tipo: Patinete eléctrico | Vel. max: {self.vel_max}km/h"

v1 = BicicletaElectrica("B-101", 85, 6)
v2 = PatineteElectrico("P-202", 60, 25)
flota = [v1, v2]
for v in flota:
    print(v.estado())