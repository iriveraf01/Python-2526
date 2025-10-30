# Ejercicio 1
# Lea dos números enteros que serán los operandos de la operación (operando1 y
# operando2).
# Lea un tercer número que identificará la operación.
# Si operación es 0 calcula la suma de ambos operandos y muestra el resultado.
# Si operación es 1 calcula la resta. Si operación es 2 calcula la multiplicación.
# Si operación es 3 calcula la división.
# Si operación no coincide con ningún valor válido mostrará un mensaje de error.

# operando1 = int(input("Ingrese el primer número entero: "))
# operando2 = int(input("Ingrese el segundo número entero: "))
# operacion = int(input("Ingrese la operación a realizar (0: suma, 1: resta, 2: multiplicación, 3: división): "))
# if operacion == 0:
#     resultado = operando1 + operando2
#     print(f"La suma de {operando1} y {operando2} es: {resultado}")
# elif operacion == 1:
#     resultado = operando1 - operando2
#     print(f"La resta de {operando1} y {operando2} es: {resultado}")
# elif operacion == 2:
#     resultado = operando1 * operando2
#     print(f"La multiplicación de {operando1} y {operando2} es: {resultado}")
# elif operacion == 3:
#     if operando2 != 0:
#         resultado = operando1 / operando2
#         print(f"La división de {operando1} entre {operando2} es: {resultado}")
#     else:
#         print("Error: No se puede dividir entre cero.")
# else:
#     print("Error: Operación no válida.")

# Ejercicio 2
# Realizar un algoritmo para determinar, de N cantidades introducidas por teclado:
# - La media aritmética.
# - El número más alto.
# - El número más bajo.

# num1 = int(input("Introduce un numero: "))
# num2 = int(input("Introduce un segundo numero: "))
# num3 = int(input("Introduce otro numero: "))
# numeros = (num1, num2, num3)
# print(f"Media aritmética {sum(numeros)} / {len(numeros)} = {(sum(numeros)) / len(numeros)}")
# print(f"El números más alto de entre los tres es {max(numeros)}")
# print(f"El números más bajo de entre los tres es {min(numeros)}")

# Ejercicio 3
# Este ejercicio consiste en realizar un juego de adivinar un número. El número a adivinar
# se genera al inicio del juego automáticamente mediante una función de la librería de
# Python “random” que genera números aleatorios.
# Para usar la librería es necesario importarla, recomendado al principio del código:
# import random.
# Para obtener un número entero aleatorio se usa la función “randint” que recibe por
# parámetro el rango entre el cual generar el número aleatorio. Por ejemplo, un número
# aleatorio del 1 al 10 sería: random.randint(1,10)
# El juego consiste en lo siguiente:
# - Pedir al usuario que ingrese la dificultad del juego, esta será un número del 10 al 50.
# Este número será utilizado para generar el número aleatorio.
# - Pedir al usuario que adivine el número generado.
# - El usuario tiene un máximo de 4 intentos para adivinar el número.
# - Si no ha acertado, informarle del error y de los intentos consumidos. También
# comunicarle una “pista” diciéndole si el número a adivinar es mayor o menor al
# introducido.
# - Si adivina el número en los 4 intentos, comunica el acierto y el número de aciertos
# consumidos, por ejemplo: “¡Correcto: has acertado el número en 3 aciertos!”
# - Si pasan los 4 intentos y no ha adivinado el número, comunicar que ha perdido el
# juego.
# - Tanto si ha acertado como si ha perdido, darle la oportunidad de jugar de nuevo,
# seleccionando una nueva dificultad.
# import random
# num = int(input("Introduce un número entre el 10 y el 50: "))
# num_aleatorio = random.randint(1, num)
# intentos = 0
# while intentos != 4:
#     pregunta = int(input(f"Intenta adivinar el número aleatorio entre el 1 y {num}: "))
#     intentos += 1
#     if pregunta == num_aleatorio:
#         print(f"Correcto: has acertado el número ({num_aleatorio}) en {intentos} aciertos!")
#         break
#     else:
#         print(f"Error: Número incorrecto llevas {intentos} intentos.")
#         if pregunta > num_aleatorio:
#             print("Pista: El número es menor.")
#         else:
#             print("Pista: El número es mayor.")


# Ejercicio 4
# Realiza una función que reciba un número entero positivo N y muestre en pantalla un
# patrón de asteriscos con N filas como en el siguiente ejemplo para N=7
# *
# **
# ***
# ****
# *****
# ******
# *******
# def asteriscos(n):
#     for i in range(1, n + 1):
#         print('*' * i)
# asteriscos(7)