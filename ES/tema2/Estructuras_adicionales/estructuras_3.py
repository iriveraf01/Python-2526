from collections import namedtuple, defaultdict

# Definición del namedtuple con 3 campos.
Alumno = namedtuple('Alumno', ['nombre', 'grupo', 'nota'])

# Variable global
lista_alumnos = []

def insertar_alumno(nombre, grupo, nota):
    """Crea un objeto Alumno y lo añade a la lista global."""

    # Creamos el nuevo alumno a través del namedtuple
    nuevo_alumno = Alumno(nombre, grupo, nota)
    # Se añade a la lista si no existe
    if nuevo_alumno not in lista_alumnos:
        lista_alumnos.append(nuevo_alumno)
    else:
        print("El alumno ya existe")

def mayor_nota():
    """Busca el alumno con la nota más alta."""
    # Si la lista está vacía
    if not lista_alumnos:
        print("No existen alumnos")
    # Dado que es una lista de tuplas, no podemos hacer max(lista)
    # Usamos max con una función lambda para comparar por el campo nota
    # La función lambda recibe la tupla y devuelve el campo nota de la tupla
    mejor = max(lista_alumnos, key=lambda a: a.nota)
    print(f"Alumno con mayor nota: Nombre: {mejor.nombre}, Grupo: {mejor.grupo}, Nota: {mejor.nota}")

def media_grupos():
    """Calcula la media de notas por grupo y las retorna en forma de dict."""
    # Agrupamos notas por grupo en un diccionario de listas -> {grupo:[notas]}
    # Para construir este diccionario usamos un defaultdict de listas
    grupos_datos = defaultdict(list)
    for alumno in lista_alumnos:
        # Al ser un defaultdict no es necesario comprobar si la clave ya existe. 
        # Si el grupo no existe se crea con una lista vacía
        grupos_datos[alumno.grupo].append(alumno.nota)
    
    # Una vez tenemos las notas agrupadas por grupos Calculamos la media
    medias = {}
    for grupo, notas in grupos_datos.items():
        medias[grupo] = sum(notas) / float(len(notas))
    
    return medias

def main():
    # Insertar alumnos de prueba
    datos_prueba = [
        ("Ana", "1A", 7.5),
        ("Luis", "1A", 6.0),
        ("Marta", "1B", 8.25),
        ("Juan", "1B", 9.0)
    ]
    
    for d in datos_prueba:
        insertar_alumno(d[0], d[1], d[2])
    
    print("--- Resultados ---")
    # Probar mayor nota
    mayor_nota()
    
    # Probar medias por grupo
    medias = media_grupos()
    for grupo, media in medias.items():
        print("Media del grupo {}: {}".format(grupo, media))

if __name__ == "__main__":
    main()