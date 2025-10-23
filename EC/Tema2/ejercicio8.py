# Ejercicio 8
# Haz un programa que pida dos números y muestre su división.
# Debe controlar que el usuario escriba números válidos y no divida entre cero.

try:
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))
    print(a / b)
except ValueError:
    print("Debes introducir solo números.")
except ZeroDivisionError:
    print("No puedes dividir entre cero.")