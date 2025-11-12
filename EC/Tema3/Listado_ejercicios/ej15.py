# list_cities = [
#  Ciudad("Bogotá", 8000000, "Colombia", "América"),
#  Ciudad("Lima", 10000000, "Peru", "America"),
#  Ciudad("Paris", 5000000, "Francia", "Europa"),
#  Ciudad("Berlin", 4000000, "Alemania", "Europa"),
#  Ciudad("Tokio", 9000000, "Japón", "Asia"),
#  Ciudad("Sydney", 3000000, "Australia", "Oceanía"),
#  Ciudad("Johannesburgo", 5000000, "Sudáfrica", "África"),
#  Ciudad("Moscú", 10000000, "Rusia", "Europa"),
#  Ciudad("Nueva York", 8000000, "Estados Unidos", "América"),
#  Ciudad("Sao Paulo", 12000000, "Brasil", "América"),
#  Ciudad("Buenos Aires", 15000000, "Argentina", "América"),
#  Ciudad("Londres", 9000000, "Reino Unido", "Europa"),
#  Ciudad("Roma", 4000000, "Italia", "Europa"),
#  Ciudad("Pekín", 20000000, "China", "Asia"),
#  Ciudad("Delhi", 15000000, "India", "Asia"),
#  Ciudad("El Cairo", 7000000, "Egipto", "África"),
#  Ciudad("Ciudad del Cabo", 4000000, "Sudáfrica", "África"),
#  Ciudad("Melbourne", 5000000, "Australia", "Oceanía"),
#  Ciudad("Auckland", 2000000, "Nueva Zelanda", "Oceanía"),
#  Ciudad("Brisbane", 3000000, "Australia", "Oceanía"),
#  Ciudad("Madrid", 6000000, "España", "Europa"),
#  Ciudad("Lisboa", 3000000, "Portugal", "Europa"),
#  ]
# 15. Diseña una aplicación Python que gestione una lista de ciudades.
# De cada ciudad se guarda nombre, población, país y continente. Se considera
# que dos ciudades son iguales si tienen el mismo nombre y país.
# La gestión de ciudades incluirá la creación de una clase que contenga métodos para:
# - Mostrar las ciudades de un continente dado.
# - Mostrar las ciudades con una población mayor que un número dado.
# - Retornar el número de ciudades de un país dado.
# - Retornar el número de ciudades que contienen una cadena en su nombre.
# - Retornar la media de la población de las ciudades de un país.
# - Retornar una lista con las ciudades de un país.
# - Retornar una lista con las ciudades de un continente.
# - Retornar la suma de los habitantes de todas las ciudades.
# - Añadir ciudad. Este método recibe un objeto ciudad como parámetro e intenta
# añadir esa ciudad a la lista. Si la ciudad está en la lista no podrá añadirla y
# retornará False. En caso de añadirla el retorno será True. Para comprobar si
# un valor está en una lista se puede utilizar:
# - if valor in lista
# - if valor not in lista
class Ciudad:
    def __init__(self,nombre, poblacion, pais, continente):
        self.nombre = nombre
        self.poblacion = poblacion
        self.pais = pais
        self.continente = continente
    
    def __eq__(self, otro):
        if isinstance(otro, Ciudad):
            return self.nombre == otro.nombre and self.pais == otro.pais
        return False 
    
    def __str__(self):
        return f"{self.nombre}, {self.pais}, {self.continente} - Población: {self.poblacion}"

class GestionCiudad:
    list_cities = []
    @classmethod
    def mostrar_ciudades_por_continente(cls, continente):
        ciudades_continente = []
        for ciudad in cls.list_cities:
            if ciudad.continente.lower() == continente.lower():
                ciudades_continente.append(ciudad)
        return ciudades_continente

    @classmethod
    def mostrar_ciudades_mayores_a(cls, habitantes):
        ciudades_mayores = []
        for ciudad in cls.list_cities:
            if ciudad.poblacion > habitantes:
                ciudades_mayores.append(ciudad)
        return ciudades_mayores
    
    @classmethod
    def numero_ciudades_de_un_pais(cls, pais):
        ciudades_pais = []
        for ciudad in cls.list_cities:
            if ciudad.pais == pais:
                ciudades_pais.append(ciudad)
        return len(ciudades_pais)
    
    @classmethod
    def media_poblacion_de_un_pais(cls, pais):
        total_poblacion = 0
        contador = 0
        for ciudad in cls.list_cities:
            if ciudad.pais == pais:
                total_poblacion += ciudad.poblacion
                contador += 1
        if contador == 0:
            return 0
        return total_poblacion / contador
    
    @classmethod
    def retornar_lista_ciudades_de_un_pais(cls, pais):
        ciudades_pais = []
        for ciudad in cls.list_cities:
            if ciudad.pais == pais:
                ciudades_pais.append(ciudad)
        return ciudades_pais
    
    @classmethod
    def retornar_lista_ciudades_de_un_continente(cls, continente):
        ciudades_continente = []
        for ciudad in cls.list_cities:
            if ciudad.continente == continente:
                ciudades_continente.append(ciudad)
        return ciudades_continente
    
    @classmethod
    def sumar_habitantes(cls):
        total_habitantes = 0
        for ciudad in cls.list_cities:
            total_habitantes += ciudad.poblacion
        return total_habitantes
    
    @classmethod
    def añadir_ciudad(cls, ciudad):
        if ciudad in cls.list_cities:
            return False
        cls.list_cities.append(ciudad)
        return True

list_cities = [
    Ciudad("Bogotá", 8000000, "Colombia", "América"),
    Ciudad("Lima", 10000000, "Peru", "America"),
    Ciudad("Paris", 5000000, "Francia", "Europa"),
    Ciudad("Berlin", 4000000, "Alemania", "Europa"),
    Ciudad("Tokio", 9000000, "Japón", "Asia"),
    Ciudad("Sydney", 3000000, "Australia", "Oceanía"),
    Ciudad("Johannesburgo", 5000000, "Sudáfrica", "África"),
    Ciudad("Moscú", 10000000, "Rusia", "Europa"),
    Ciudad("Nueva York", 8000000, "Estados Unidos", "América"),
    Ciudad("Sao Paulo", 12000000, "Brasil", "América"),
    Ciudad("Buenos Aires", 15000000, "Argentina", "América"),
    Ciudad("Londres", 9000000, "Reino Unido", "Europa"),
    Ciudad("Roma", 4000000, "Italia", "Europa"),
    Ciudad("Pekín", 20000000, "China", "Asia"),
    Ciudad("Delhi", 15000000, "India", "Asia"),
    Ciudad("El Cairo", 7000000, "Egipto", "África"),
    Ciudad("Madrid", 6000000, "España", "Europa"),
    Ciudad("Ciudad del Cabo", 4000000, "Sudáfrica", "África"),
    Ciudad("Melbourne", 5000000, "Australia", "Oceanía"),
    Ciudad("Auckland", 2000000, "Nueva Zelanda", "Oceanía"),
    Ciudad("Brisbane", 3000000, "Australia", "Oceanía"),
    Ciudad("Lisboa", 3000000, "Portugal", "Europa"),
]
for ciudad in list_cities:
    GestionCiudad.list_cities.append(ciudad)

print("Ciudades en Europa:")
ciudades_europa = GestionCiudad.mostrar_ciudades_por_continente("Europa")
for ciudad in ciudades_europa:
    print(ciudad)
print("###\t###")
ciudades_3000000 = GestionCiudad.mostrar_ciudades_mayores_a(3000000)
for ciudad in ciudades_3000000:
    print(ciudad)
print("###\t###")
ciudades_australia = GestionCiudad.numero_ciudades_de_un_pais("Australia")
print(f"Número de ciudades en Australia: {ciudades_australia}")
print("###\t###")
media_poblacion_india = GestionCiudad.media_poblacion_de_un_pais("India")
print(f"Media de población en India: {media_poblacion_india}")
print("###\t###")
ciudades_argentina = GestionCiudad.retornar_lista_ciudades_de_un_pais("Argentina")
for ciudad in ciudades_argentina:
    print(ciudad)
print("###\t###")
ciudades_asia = GestionCiudad.retornar_lista_ciudades_de_un_continente("Asia")
for ciudad in ciudades_asia:
    print(ciudad)
print("###\t###")
total_habitantes = GestionCiudad.sumar_habitantes()
print(f"Suma total de habitantes en todas las ciudades: {total_habitantes}")
print("###\t###")
nueva_ciudad = Ciudad("Barcelona", 5500000, "España", "Europa")
resultado_añadir = GestionCiudad.añadir_ciudad(nueva_ciudad)
print(f"¿Se añadió Barcelona? {resultado_añadir}")