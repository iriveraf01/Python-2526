
def agregar_persona(personas: dict, nombre, apellido, telefono):
    # Si el diccionario está vacío, el ID será 1111
    if personas == {}:
        nuevo_id = 1111
    # Si no, se obtiene el ID más grande y se suma 1
    else:
        nuevo_id = max(personas.keys()) + 1

    # Se agrega la persona al diccionario y se retorna
    personas[nuevo_id] = (nombre, apellido, telefono)
    

def obtener_persona(personas: dict, persona_id):
    return(personas.get(persona_id))

def buscar_persona(personas: dict, nombre, apellido):
    # Recorremos el diccionario comprobando si el nombre y apellido coinciden
    for id, datos in personas.items():
        # Desempaquetamos la tupla de datos. 
        # _ es la variable anónima para el teléfono porque no es necesario
        datos_nombre, datos_apellido, _ = datos
        # Comparamos con los parámetros recibidos
        if datos_nombre == nombre and datos_apellido == apellido:
            return id
    # Si no se encuentra, se retorna None
    return None
        

def agregar_evento(eventos: dict, nombre_evento):
    # Comprobamos si el evento existe
    if nombre_evento in eventos:
        return False
    # Si no existe, se agrega un conjunto vacío de participantes a la clave
    eventos[nombre_evento] = set()
    return True

def agregar_participante(eventos: dict, nombre_evento, participante_id):
    # Si el evento no está en el diccionario, retorna None
    if nombre_evento not in eventos:
        return False
    # Si el evento existe, se agrega el participante al conjunto de participantes con el método add de los conjuntos
    eventos[nombre_evento].add(participante_id)
    return True

def eventos_comunes(eventos: dict, personas: list):
    # Recorremos los eventos y comprobamos si los IDS recibidos es un subconjunto de los IDS participantes
    # Si es un subconjunto, se agrega el evento al conjunto de eventos comunes
    # Al final se retorna el conjunto de eventos comunes
    comunes = set()
    set_personas = set(personas)
    for evento, participantes in eventos.items():
        # Si los IDS recibidos son un subconjunto de los participantes, se agrega el evento al resultado
        if set_personas.issubset(participantes):
            comunes.add(evento)
    return tuple(comunes)

    # Lo mismo pero con comprensión de conjuntos
    #return {evento for evento, participantes in eventos.items() if set(ids).issubset(participantes)}

def evento_mayor(eventos: dict):
    # Recorremos el diccionario y guardamos el máximo de participantes
    # En cada iteracción comparamos si el número de participantes es mayor al máximo
    # Si es mayor, actualizamos el máximo y guardamos el evento
    maximo = None
    partipantes = 0

    for evento, participantes in eventos.items():
        if len(participantes) > partipantes:
            maximo = evento
            partipantes = len(participantes)
    return (maximo, participantes)
  
    