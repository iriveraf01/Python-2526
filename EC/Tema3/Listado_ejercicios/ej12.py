# 12. Diseñar una aplicación Python que trabaje con objetos de la clase “Partido”. Cada
# partido tendrá como atributos equipo local, equipo visitante, goles local, goles
# visitante, campeonato y fecha.
# La aplicación consta también de una clase llamada “GestionPartidos” que tendrá como
# atributo de clase una lista de partidos y los métodos siguientes:
#   - Filtrar por equipo local. Recibe un equipo local como argumento e imprime
#     todos los partidos de ese equipo actuando como local.
#   - Ganados del equipo. Recibe un equipo como argumento y retorna cuántos
#     partidos ganó ese equipo, independientemente de si actuó como local o como
#     visitante.
#   - Mostrar los partidos del año pasado como parámetro.
#   - Mostrar los partidos de una fecha pasada como parámetro.
#   - Añadir un nuevo partido a la lista de partidos.
#   - Cuenta partidos. Retorna el número de partidos de la lista.
# Prueba las clases y los métodos creados.

class Partido:
    def __init__(self, equipo_local, equipo_visitante, goles_local, goles_visitante, campeonato, fecha):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.goles_local = goles_local
        self.goles_visitante = goles_visitante
        self.campeonato = campeonato
        self.fecha = fecha

class GestionPartido:
    lista_partidos = []

    @classmethod
    def filtrar_equipo_local(cls, local):
        for partido in cls.lista_partidos:
            if partido.equipo_local == local:
                print(f"{partido.equipo_local} vs {partido.equipo_visitante} - {partido.goles_local}:{partido.goles_visitante} - {partido.campeonato} - {partido.fecha}")

    @classmethod
    def ganados_del_equipo(cls, equipo):
        contador = 0
        for partido in cls.lista_partidos:
            if (partido.equipo_local == equipo and partido.goles_local > partido.goles_visitante) or \
            (partido.equipo_visitante == equipo and partido.goles_visitante > partido.goles_local):
                contador += 1
        return f"El {equipo} ha ganado {contador} veces."
    
    @classmethod
    def mostrar_partidos_por_año(cls, año):
        año_str = str(año)
        partidos_año = []
        for partido in cls.lista_partidos:
            if partido.fecha.split("-")[0] == año_str:
                partidos_año.append(partido)
        return partidos_año
    
    @classmethod
    def mostrar_partidos_por_fecha(cls, fecha):
        partidos_fecha = []
        for partido in cls.lista_partidos:
            if partido.fecha == fecha:
                partidos_fecha.append(partido)
        return partidos_fecha
    
    @classmethod
    def añadir_partidos(cls, equipo_local, equipo_visitante, goles_local, goles_visitante, campeonato, fecha):
        nuevo_partido = Partido(equipo_local, equipo_visitante, goles_local, goles_visitante, campeonato, fecha)
        cls.lista_partidos.append(nuevo_partido)
        print("Añadido.")
    
    @classmethod
    def cuenta_partidos(cls):
        return len(cls.lista_partidos)


Partido1 = Partido("EquipoA", "EquipoB", 2, 1, "Campeonato1", "2023-05-10")
Partido2 = Partido("EquipoC", "EquipoA", 0, 3, "Campeonato1", "2023-06-15")
GestionPartido.lista_partidos.append(Partido1)
GestionPartido.lista_partidos.append(Partido2)
print("############")
GestionPartido.filtrar_equipo_local("EquipoA")
print("############")
print(GestionPartido.ganados_del_equipo("EquipoA"))
print("############")
GestionPartido.añadir_partidos("EquipoD", "EquipoE", 1, 1, "Campeonato2", "2023-07-20")
print("############")
partidos_2023 = GestionPartido.mostrar_partidos_por_año(2023)
for p in partidos_2023:
    print(f"{p.equipo_local} vs {p.equipo_visitante} - {p.goles_local}:{p.goles_visitante} - {p.campeonato} - {p.fecha}")
print("############")
fecha = GestionPartido.mostrar_partidos_por_fecha("2023-05-10")
for p in fecha:
    print(f"{p.equipo_local} vs {p.equipo_visitante} - {p.goles_local}:{p.goles_visitante} - {p.campeonato} - {p.fecha}")
print("############")
print(f"Número de partidos: {GestionPartido.cuenta_partidos()}")
print("############")