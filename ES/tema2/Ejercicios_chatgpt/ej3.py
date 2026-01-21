# a)
#   Obtén un conjunto con todas las personas que han vendido en algún mes.
# b)
#   Obtén el conjunto de personas que han vendido en todos los meses.
# c)
#   Obtén las personas que han vendido en exactamente un mes.
# d)
#   Crea un nuevo diccionario llamado frecuencia donde:
#       La clave sea el nombre de la persona
#       El valor sea el número de meses en los que ha vendido

ventas = {
    "enero": {"Ana", "Luis", "Marta"},
    "febrero": {"Luis", "Pedro"},
    "marzo": {"Ana", "Marta", "Pedro", "Luis"}
}
personas = set()
for v in ventas.values():
    for nombres in v:
        personas.add(nombres)

print(personas)