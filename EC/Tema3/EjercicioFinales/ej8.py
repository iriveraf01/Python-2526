# Ejercicio 8 - Clases abstractas (Tema: Pasarela de pago digital)
# Una plataforma necesita validar distintos métodos de pago. Todos los métodos de pago
# deben implementar la misma interfaz:
# • procesar_pago(cantidad: float)
# • obtener_nombre() → nombre del método
# Se pide:
# 1. Crear una clase abstracta MetodoPago utilizando ABC y @abstractmethod.
# 2. Crear las clases:
# • TarjetaCredito: con atributos “titular” y “número”. Métodos:
# - procesar_pago: muestra “Procesando pago de X€(con 2
# decimales) con tarjeta de X(titular) y retorna True.
# - obtener_nombre: retorna “Tarjeta de crédito”.
# • Bizum: con atributo “teléfono”. Métodos:
# - procesar_pago: muestra “Procesando Buzum de X€(con 2
# decimales) al TLF y retorna true.
# - obtener_nombre: retorna “Bizum”.
# • TransferenciaBancaria: con atributo “iban”. Métodos:
# - procesar_pago: muestra “Ordenando transferencia de X€(con 2
# decimales) al IBAN X y retorna true.
# - obtener_nombre: retorna “Transferencia bancaria”.
# 3. Cada método de pago debe implementar los métodos obligatorios.
# 4. Crear una función llamada realizar_cobro(metodo: MetodoPago, cantidad:
# float) que:
# • muestre el nombre del método: “Intentando cobrar con X”
# • intente procesar el pago.
# • muestre un mensaje "Pago aceptado" o “Pago rechazado”
# 5. Crear una lista con distintos métodos de pago y probarlos todos.
from abc import ABC, abstractmethod

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, cantidad) -> float:
        pass

    @abstractmethod
    def obtener_nombre(self):
        pass

class TarjetaCredito(MetodoPago):
    def __init__(self, titular, numero):
        self.titular = titular
        self.numero = numero

    def procesar_pago(self, cantidad):
        print(f"Procesando pago de {cantidad}€ con tarjeta de {self.titular} y número {self.numero}.")
        return True

    def obtener_nombre(self):
        return "Tarjeta de crédito."
    
class Bizum(MetodoPago):
    def __init__(self, telefono):
        self.telefono = telefono
    
    def procesar_pago(self, cantidad):
        print(f"Procesando Bizum de {cantidad}€ al TLF({self.telefono}).")
        return True
    
    def obtener_nombre(self):
        return "Bizum."
    
class TransferenciaBancaria(MetodoPago):
    def __init__(self, iban):
        self.iban = iban
    
    def procesar_pago(self, cantidad):
        print(f"Ordenando transferencia de {cantidad}€ al IBAN ({self.iban}).")
        return True
    
    def obtener_nombre(self):
        return "Transferencia bancaria."
    
def realizar_cobro(MetodoPago, cantidad):
    print(f"Intentando cobrar con {MetodoPago.obtener_nombre()}")
    if MetodoPago.procesar_pago(cantidad):
        print("Pago aceptado.")
    else:
        print("Pago rechazado.")
    

metodos: list[MetodoPago] = [
    TarjetaCredito("Ana Pérez", "1111 2222 3333 4444"),
    Bizum("600123123"),
    TransferenciaBancaria("ES76 2100 1234 5601 2345 6789"),
]
for m in metodos:
    realizar_cobro(m, 49.99)