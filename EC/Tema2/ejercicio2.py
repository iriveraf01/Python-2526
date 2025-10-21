# Ejercicio 2
# Pide al usuario si desea continuar (solo podrá responder “S” o “N” (tanto en
# mayúsculas como en minúsculas), si el usuario introduce otra letra que no sea alguna
# de esas 2, dará el error “Respuesta no válida, introduce S o N”, si la respuesta es S
# mostrará “Continuamos…” y si es N mostrará “Fin del programa”.

respuesta = ""
while respuesta != "N":
    respuesta = input("Desea continuar: (s/n) ").upper()
    if respuesta not in ("S/N"):
        print("Respuesta no válida, introduce S o N.")
    elif respuesta in "S":
        print("Continuamos...")
    else:
        print("Fin del programa.")

