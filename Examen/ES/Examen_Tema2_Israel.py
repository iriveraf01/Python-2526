def agregar_jugadores(goleadores: dict, jugador:str, equipo:str, posicion:str, goles:int):
    if jugador in goleadores.keys():
        return False
    goleadores[jugador] = (equipo, posicion, goles)
    return True

def actualizar_goles(goleadores: dict, jugador:str, goles:int):
    if jugador not in goleadores.keys():
        return False
    for nombre,datos in goleadores.items():
        if jugador == nombre:
            goleadores[jugador] = (datos[0], datos[1], goles)
            return True
        

def max_goles_pos(goleadores:dict, posicion:str):
    nombre_mayor_goleador = []
    mas_goles = 0
    for nombre, datos in goleadores.items():
        # si la posicion es igual
        if posicion == datos[1]:
            # si los goles mayores que 0
            if datos[2] > mas_goles:
                # 0 es igual a los goles que haya
                mas_goles = datos[2]
                if datos[2] == mas_goles:
                    nombre_mayor_goleador = []
                nombre_mayor_goleador.append(nombre)
            elif datos[2] == mas_goles:
                nombre_mayor_goleador.append(nombre)
    if nombre_mayor_goleador:
        return (mas_goles, nombre_mayor_goleador)
    return None


def mostrar_jugadores_por_equipo(goleadores: dict):
    nuevo_dic = {}
    for nombre, datos in goleadores.items():
        nuevo_dic[datos[0]] = (nombre, datos[1], datos[2])
    print(sorted(nuevo_dic.items()))

def main():
    jugadores = {
        "Valverde": ("Real Madrid", "Medio", 5),
        "Mbappe": ("Real Madrid", "Delantero", 25),
        "Raphinha": ("Barcelona", "Extremo", 13),
        "Lewandowski": ("Barcelona", "Delantero", 25),
        "Vinicius": ("Real Madrid", "Extremo", 13),
        "Griezmann": ("Atletico Madrid", "Delantero", 6)
    }
    print("--- AGREGAR JUGADORES ---")
    print(agregar_jugadores(jugadores, "Raphinha", "Barcelona", "Extremo", 13))
    print(agregar_jugadores(jugadores, "Messi", "Inter Miami", "Extremo", 50))
    print(jugadores)
    print("-------------------------------------------------------------------------")

    print("--- ACTUALIZAR GOLES DE UN JUGADOR ---")
    print(actualizar_goles(jugadores, "Raphinha", 2))
    print(jugadores)
    print("-------------------------------------------------------------------------")
    
    print("--- MÁXIMO GOLEADOR POR POSICIÓN ---")
    print(max_goles_pos(jugadores, "Delantero"))
    print("-------------------------------------------------------------------------")

    print("--- MOSTRAR JUGADORES POR EQUIPO ---")
    mostrar_jugadores_por_equipo(jugadores)

if __name__ == "__main__":
    main()