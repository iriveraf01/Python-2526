# Ejercicio 1
# Crea una función que pida al usuario:
# 1º: Divisor: Un entero que servirá para comprobar si un número es múltiplo de el o no.
# 2º: Una vez establecido el divisor, se le pedirá al usuario que introduzca números
# enteros.
# El programa debe calcular si el número introducido es múltiplo o no de "divisor". El
# programa acaba cuando se introduce el 0.
# 3º: Al finalizar, se muestran cuantos números son múltiplos de divisor y cuantos no lo
# son. El 0 no debe tenerse en cuenta como múltiplo ni como no múltiplo.
# No es necesario verificar y asegurar que se introducen realmente enteros.
# La salida por pantalla debe ser así:
#  Introduce un divisor (entero): 3
#  Introduce un número entero (0 para terminar): 6
#  Introduce un número entero (0 para terminar): 9
#  Introduce un número entero (0 para terminar): 2
#  Introduce un número entero (0 para terminar): 1
#  Introduce un número entero (0 para terminar): 0
#  Números múltiplos de 3: 2
#  Números no múltiplos de 3: 2
def ej1():
    divisor = int(input("Introduce un divisor (entero): "))
    numero = 1
    contador_multiplos = 0
    contador_no_multiplos = 0
    while numero != 0:
        numero = int(input("Introduce un número entero (0 para terminar): "))
        if numero % divisor == 0 and numero != 0:
            contador_multiplos += 1
        elif numero != 0:
            contador_no_multiplos += 1
    print(f"Números múltiplos de {divisor}: {contador_multiplos}")
    print(f"Números no múltiplos de {divisor}: {contador_no_multiplos}")
    
ej1()