CONTRASENAS_PROHIBIDAS = ["12345678", "password", "qwertyui", "letmein1", "welcome"]
# Ejercicio 3
# Crea una función llamada procesar_password(password) que analice una contraseña.
# Para mejorar la seguridad, la contraseña real comienza a partir de la primera letra "a" y
# a partir de esa letra, se cuentan 8 caracteres.
# Además, existirá una lista de contraseñas prohibidas que no se pueden usar.
# Mensajes de error:
# "Error: La contraseña debe contener al menos una letra 'a' seguida de más caracteres."
# "Error: La contraseña generada está en la lista de contraseñas prohibidas."
def procesar_password(password: str) -> str:
    indice = password.find("a")
    
    if indice == -1 or len(password) - indice < 8:
        return "Error: La contraseña debe contener al menos una letra 'a' seguida de más caracteres."

    contraseña_generada = password[indice : indice + 8]

    for prohibida in CONTRASENAS_PROHIBIDAS:
        if prohibida in contraseña_generada:
            return "Error: La contraseña generada está en la lista de contraseñas prohibidas."

    return contraseña_generada

# Prueba
password_test = "banana12345678"
password_test_mal = "bapasswordnana12345678"
resultado_bien = procesar_password(password_test)
resultado_mal = procesar_password(password_test_mal)
print("\n--- EJERCICIO: PROCESAMIENTO DE CONTRASEÑA ---")
print(f"Contraseña original: {password_test}")
print(f"Resultado del procesamiento: {resultado_bien}")
print("\n--- EJERCICIO: PROCESAMIENTO DE CONTRASEÑA ---")
print(f"Contraseña original: {password_test_mal}")
print(f"Resultado del procesamiento: {resultado_mal}\n")