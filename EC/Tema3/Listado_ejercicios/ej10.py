# 10. Diseñar una clase llamada “Mates” con los métodos estáticos que se describen:
# a. mayor. Recibe dos números como argumento y retorna el mayor.
# b. producto. Recibe tres números como argumento y retorna su producto.
# c. potencia. Recibe una base y un exponente como argumentos y retorna la base
# elevada al exponente.
# Probar los métodos programados.
class Mates:
    @staticmethod
    def mayor(numero1, numero2):
        return numero1 if numero1 > numero2 else numero2
    
    @staticmethod
    def producto(numero1, numero2, numero3):
        return numero1 * numero2 * numero3
    
    @staticmethod
    def potencia(base, exponente):
        return base ** exponente
print(Mates.mayor(5, 10))
print(Mates.producto(2, 3, 4))
print(Mates.potencia(2, 3))