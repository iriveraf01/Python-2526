# Ejercicio 2.
# Escribe un programa que pida al usuario dos números, los sume y muestre el resultado
# junto con su tipo de dato.

numero1 = input("Dame un número: ")
numero2 = input("Dame otro número: ")
suma = int(numero1) + int(numero2)
print(f"La suma de los numeros es de {str(suma)} y su tipo es {type(suma)}")

print(f"\nLa suma de los numeros es de {int(numero1) + int(numero2)} y su tipo es {type(int(numero1) + (int(numero2)))}")
