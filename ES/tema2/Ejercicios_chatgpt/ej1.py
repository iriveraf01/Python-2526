# a)
#     Crea un diccionario llamado alumnos donde:
#         La clave sea el nombre
#         El valor sea una tupla con la edad y el grupo
#         (Si un nombre aparece varias veces, conserva solo el último).
# b)
#     A partir del diccionario alumnos, crea otro diccionario llamado grupos donde:
#         La clave sea el grupo
#         El valor sea un conjunto con los nombres de los alumnos de ese grupo
# c)
#     Muestra por pantalla el grupo o grupos que tengan más de un alumno.
# d)
#     Usando únicamente operaciones de conjuntos, obtén el conjunto de alumnos que:
#         Están en el grupo "A" pero no en el "C".
datos = (
    ("Ana", 20, "A"),
    ("Luis", 22, "B"),
    ("Marta", 19, "A"),
    ("Pedro", 21, "C"),
    ("Luis", 23, "A")
)
alumnos = {}
for nombre, edad, curso in datos:
    alumnos[nombre] = (edad, curso)
print(alumnos)

grupos = {}
for clave, valor in alumnos.items():
    curso = valor[1] # Curso
    if curso not in grupos:
        grupos[curso] = set()
    grupos[curso].add(clave)
print(grupos)

for c, v in grupos.items():
    if len(v) > 1:
        print(f"El grupo {c} tiene {len(v)} alumnos.")

alumnos_A = grupos.get("A", set())
alumnos_C = grupos.get("C", set())
alumnos_A_sin_C = alumnos_A - alumnos_C
print("Alumnos en el grupo A pero no en el C:", alumnos_A_sin_C)