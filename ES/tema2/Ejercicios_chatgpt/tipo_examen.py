# ● agregar_alumno
#     Parámetros:
#         Diccionario de alumnos
#         Nombre
#         Email
#     Acción:
#         Añade el alumno al diccionario
#         El ID se genera automáticamente empezando por 2001
#         Cada nuevo alumno incrementa el ID en 1
#     Retorno:
#         ID del alumno creado

def agregar_alumno(dic_alumnos, nombre, email):
    if not dic_alumnos:
        nuevo_id = 2001
    else:
        nuevo_id = max(dic_alumnos.keys()) + 1
    
    dic_alumnos[nuevo_id] = (nombre, email)

    return f"Se ha introducido el alumno con ID {nuevo_id}."
# Ejemplo de uso
alumnos = {}
print(agregar_alumno(alumnos, "Juan", "Peréz"))
print(agregar_alumno(alumnos, "Ana", "García"))
print(alumnos)

# ● obtener_alumno
#     Parámetros:
#         Diccionario de alumnos
#         ID
#     Acción:
#         Busca el ID en el diccionario
#     Retorno:
#         Tupla con los datos del alumno o None si no existe
def obtener_alumno(dic_alumnos, id):
    for c, v in dic_alumnos.items():
        if c == id:
            return f"Nombre: {v[0]}, apellido: {v[1]}"
        return None
print(obtener_alumno(alumnos, 2001))
print(obtener_alumno(alumnos, 2000))

# ● crear_curso
#     Parámetros:
#         Diccionario de cursos
#         Nombre del curso
#     Acción:
#         Crea un nuevo curso vacío (sin alumnos)
#         Comprueba que el curso no exista
#     Retorno:
#         True si se crea
#         False si ya existía
def crear_curso(dic_cursos, nombre_curso):
    if nombre_curso in dic_cursos:
        return False
    dic_cursos[nombre_curso] = []
    return True
cursos = {}
print(crear_curso(cursos, "1º"))
print(crear_curso(cursos, "2º"))

# ● inscribir_alumno
#     Parámetros:
#         Diccionario de cursos
#         Nombre del curso
#         ID del alumno
#     Acción:
#         Inscribe al alumno en el curso indicado
#         El curso debe existir
#     Retorno:
#         True si se inscribe correctamente
#         False si el curso no existe
def inscribir_alumno(dic_cursos, nombre_curso, id_alumno):
    if nombre_curso not in dic_cursos:
        return False
    dic_cursos[nombre_curso].append(id_alumno)
    return True
print(inscribir_alumno(cursos, "1º", 2001))
print(inscribir_alumno(cursos, "1º", 2002))
print(inscribir_alumno(cursos, "1º", 2003))
print(inscribir_alumno(cursos, "2º", 2001))

# ● cursos_comunes
#     Parámetros:
#         Diccionario de cursos
#         Lista de IDs de alumnos
#     Acción:
#         Busca los cursos en los que están inscritos todos los alumnos indicados
#     Retorno:
#         Tupla con los nombres de los cursos comunes
#         Tupla vacía si no hay ninguno
def cursos_comunes(dic_cursos, lista_ids):
    cursos_comunes = []
    for curso, ids in dic_cursos.items():
        if all(id in ids for id in lista_ids):
            cursos_comunes.append(curso)
    return tuple(cursos_comunes)
print(cursos_comunes(cursos, [2001]))

# ● curso_mas_alumnos
#     Parámetros:
#         Diccionario de cursos
#     Acción:
#         Busca el curso con mayor número de alumnos inscritos
#     Retorno:
#         Tupla (nombre_curso, número_alumnos)
def cursos_mas_alumnos(dic_cursos):
    max_alumnos = 0
    curso_mas_popular = None
    for curso, alumnos in dic_cursos:
        if len(alumnos) > max_alumnos:
            max_alumnos = len(alumnos)
            curso_mas_popular = curso
    return (curso_mas_popular, max_alumnos)
print(cursos_mas_alumnos(cursos))