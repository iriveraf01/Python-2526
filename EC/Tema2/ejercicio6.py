# Ejercicio 6
# Crea un programa que pida al usuario un número entre 1 y 10 y que:
# 1. Compruebe que el número está en ese rango (si no, pide otro).
# 2. Muestre su tabla de multiplicar.
# 3. Pregunte si desea repetir con otro número (s/n).
numero = input("Introduce un número: ")
match numero:
    case str() if numero.isdigit() and 1 <= int(numero) <= 10:
        numero = int(numero)
        while True:
            print(f"Tabla de multiplicar del {numero}:")
            for i in range(1, 11):
                print(f"{numero} x {i} = {numero * i}")
            repetir = input("¿Desea repetir con otro número? (s/n): ").lower()
            if repetir == 's':
                numero = input("Introduce un número: ")
                match numero:
                    case str() if numero.isdigit() and 1 <= int(numero) <= 10:
                        numero = int(numero)
                    case _:
                        print("Número no válido. Saliendo del programa.")
                        break
            elif repetir == 'n':
                print("Saliendo del programa.")
                break
            else:
                print("Respuesta no válida. Saliendo del programa.")
                break
    case _:
        print("Número no válido. Saliendo del programa.")   