# Ejercicio 7 - Composición (Tema: Sistema de control de riego automático)
# Se desea programar un sistema de riego automático para un invernadero.
# El sistema está formado por:
# • Un Controlador (clase principal)
# • Una Bomba de agua
# • Un SensorDeHumedad
# El controlador debe contener (composición) una instancia de Bomba y otra de Sensor.
# Comportamiento esperado:
# 1. Clase SensorDeHumedad con método obtener_humedad() que devuelve un
# número entre 0 y 100(aleatorio).
# 2. Clase Bomba con métodos:
# • encender(): pone un atributo “encendida” a True. Y muestra con un
# print “Bomba ENCENDIDA”.
# • apagar(): pone el atributo “encendida” a False. Y muestra con un print
# “Bomba APAGADA".
# • estado(): retorna ENCENDIDA si está encendida la Bomba,
# APAGADA en caso contrario.
# 3. Clase ControladorRiego:
# • contiene un SensorDeHumedad y una Bomba.
# • método ciclo_control():
# - Imprime: “Humedad actual del suelo X %”
# - si humedad < 40: enciende la bomba
# - si humedad ≥ 40: apaga la bomba
# - imprime el estado resultante: “Estado de la bomba: X”
# Se pide crear las clases y ejecutar dos ciclos de prueba.
class SensorDeHumedad:
    def obtener_humedad(self):
        import random
        return random.randint(0, 100)
    
class Bomba:
    def __init__(self):
        self.encendida = True

    def encender(self):
        self.encendida = True
        print("Bomba ENCENDIDA")
    def apagar(self):
        self.encendida = False
        print("Bomba APAGADA")
    def estado(self):
        if self.encendida == True:
            return "ENCENDIDA"
        else:
            return "APAGADA"

class ControladorRiego:
    def __init__(self):
        self.sensor_humedad = SensorDeHumedad()
        self.bomba = Bomba()
    
    def ciclo_control(self):
        # Hay que hacer una variable humedad pq si se hace sin variable no funciona correctamente
        humedad = self.sensor_humedad.obtener_humedad()
        print(f"Humedad actual del suelo {humedad}%")
        if humedad < 40:
            self.bomba.encender()
        else:
            self.bomba.apagar()
        print(f"Estado de la bomba: {self.bomba.estado()}")


controlador = ControladorRiego()
# Simulamos dos ciclos de control
controlador.ciclo_control()
controlador.ciclo_control()