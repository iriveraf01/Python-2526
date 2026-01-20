# Ejercicio 5 - Validación de JSON
# Escribe una función validar_usuario(json_string) que:
# 1. Intente deserializar el JSON
# 2. Verificar que sea un diccionario
# 3. Verifique que existan las claves: nombre, email, edad
# 4. Verifique que edad sea un número entre 18 y 100
# 5. Verifique que email contenga el carácter '@'
# 6. Devuelva True si es válido, False si no
# 7. Maneje json.JSONDecodeError apropiadamente
import json
def validar_usuario(json_string):
    try:
        #1
        datos = json.loads(json_string)
        #2
        if not isinstance(datos, dict):
            return False
        #3
        claves_requeridas = {'nombre', 'email', 'edad'}
        if not claves_requeridas.issubset(datos.keys()):
            return False
        #4
        edad = datos['edad']
        if not (isinstance(edad, int) and 18 <= edad <= 100):
            return False
        #5
        email = datos['email']
        if '@' not in email:
            return False
        #6
        return True
    #7
    except json.JSONDecodeError:
        return False

# Casos de prueba
print(validar_usuario('{"nombre": "Ana", "email": "ana@mail.com", "edad": 25}')) # True
print(validar_usuario('{"nombre": "Luis", "edad": 30}')) # False (falta email)
print(validar_usuario('{"nombre": "Eva", "email": "eva.com", "edad": 25}')) # False (email sin @)
print(validar_usuario('{nombre: "Juan"}')) # False (JSON inválido)