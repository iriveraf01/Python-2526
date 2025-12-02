# Ejercicio 6 - Polimorfismo (Tema: Servicio técnico de electrodomésticos)
# Se quiere diseñar una herramienta interna para probar distintos electrodomésticos del
# servicio técnico.
# Todos los electrodomésticos implementan un método llamado diagnostico(), pero su
# comportamiento es diferente según el dispositivo:
# • Lavadora → devuelve "Tambor OK – Bomba OK – Filtros OK"
# • Horno → devuelve "Resistencias OK – Sensor temperatura OK"
# • AireAcondicionado → devuelve "Compresor OK – Nivel de gas correcto"
# Se pide:
# 1. Crear las clases correspondientes.
# 2. Implementar el método diagnostico() en cada clase.
# 3. Crear una función llamada probar(electrodomestico) que reciba cualquier
# objeto y ejecute su método diagnostico(), sin comprobar su tipo.
# 4. Crear una lista con varios electrodomésticos distintos y pasar cada uno a la
# función probar().
class Lavadora:
    def diagnostico(self):
        return "Lavadora: Tambor OK - Bomba OK - Filtros OK"
    
class Horno:
    def diagnostico(self):
        return "Horno: Resistencias OK - Sensor temperatura OK"
    
class AireAcondicionado:
    def diagnostico(self):
        return "Aire acondicionado: Compresor OK - Nivel de gas correcto"

def probar(electrodomestico):
    print(electrodomestico.diagnostico())

aparatos = [
    Lavadora(),
    Horno(),
    AireAcondicionado(),
]
for a in aparatos:
    probar(a)