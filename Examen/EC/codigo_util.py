# #EJERCICIO 1
# MAPA_EMOJIS = {
#     'a': '🍎', 'b': '🎈', 'c': '🌎', 'd': '💎', 'e': '🐘', 'f': '🌸', 
#     'g': '🦒', 'h': '🏡', 'i': '💡', 'j': '🪡', 'k': '🔑', 'l': '🦁', 
#     'm': '🌙', 'n': '⛵', 'ñ': '🟤', 'o': '🟠', 'p': '🐧', 'q': '👑', 
#     'r': '🌈', 's': '⭐', 't': '🌲', 'u': '🦄', 'v': '🌋', 'w': '🌊', 
#     'x': '❌', 'y': '🟡', 'z': '🦓'
# }

# def codificar(palabra):
#     palabras = palabra.lower()
#     palabra_codificada = ""
#     for letra in palabras:
#         if letra in MAPA_EMOJIS.keys():
#             palabra_codificada += MAPA_EMOJIS[letra]
#         else:
#             palabra_codificada += letra
#     return(palabra_codificada)

# def decodificar(mensaje_emoji):
#     mapa = {emoji: letra for letra, emoji in MAPA_EMOJIS.items()}
#     palabra_descodificada = ""
#     for i in mensaje_emoji:
#         if i in mapa.keys():
#             palabra_descodificada += mapa[i]
#         else:
#             palabra_descodificada += i
#     return palabra_descodificada
# # --- PRUEBA EJERCICIO1 ---
# palabra_test = "España con ñandú 10"

# codificado = codificar(palabra_test)
# decodificado = decodificar(codificado)

# print(f"Original: {palabra_test}")
# print(f"Codificado: {codificado}")
# print(f"Decodificado: {decodificado}")

#EJERCICIO 2
# Datos de prueba
# datos_matriz = [
#     "5.1,1.0,2.5",
#     "12.3,4.0,9.1",
#     "9.9,8.0,3.0",
#     "15.0,2.1,1.1"
# ]

# def procesar_matriz(matriz_texto: list):
#     matriz = [i.split() for i in matriz_texto] 
#     print(matriz)
#     matriz_float = [j.split(",") for i in matriz for j in i]
#     matriz_filtrada = [i for i in matriz_float if float(i[0]) > 10.0]
#     print(matriz_filtrada)
    
# matriz_filtrada = procesar_matriz(datos_matriz)
# print("Filas filtradas (Primer valor > 10.0):")
# for fila in matriz_filtrada: print(f"  {fila}")
# Salida: [[12.3, 4.0, 9.1], [15.0, 2.1, 1.1]]


#EJERCICIO 3
# Tabla oficial para la letra del DNI (índice 0 a 22)
_LETRAS_DNI = "TRWAGMYFPDXBNJZSQVHLCKE" 

class Votante:
    VOTOS_TOTALES = {}
    VOTANTES_REGISTRADOS = []
    def __init__(self, nombre, apellidos, dni, edad):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.dni = dni
        self.edad = edad

        if nombre in Votante.VOTOS_TOTALES:
            Votante.VOTOS_TOTALES[nombre] += 1
        else:
            Votante.VOTOS_TOTALES[nombre] = 1

    @staticmethod
    def calcular_letra_dni(dni):
        numero = dni[0:-2] 
        resto = (int(numero) % 23)
        return _LETRAS_DNI[resto]

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, valor):
        if valor < 18:
            raise ValueError("No puede ser menor de edad.")
        self._edad = valor
        
    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self, valor):
        if len(valor) != 9:
            raise ValueError("El dni tiene que ser de 9 caracteres.")
        if not valor[0:-2].isdigit():
            raise ValueError("Tienen que ser numeros lo primero.")
        if valor[-1].isdigit():
            raise ValueError("Lo último tiene que ser una letra.")
        if Votante.calcular_letra_dni(valor[0:-2]) != valor[-1]:
            raise ValueError("La letra no es la que deberia de ser")
            
        self._dni = valor
    
    def votar(self, partido):
        if partido in self.VOTOS_TOTALES.keys():
            self.VOTANTES_REGISTRADOS.append(self.dni)

class Escrutinio:
    @staticmethod
    def mostrar_resultados(votos):
        for voto in votos:
            print(voto)

print("### PRUEBA EJERCICIO 3 ###")
# print(Votante.calcular_letra_dni("46889241S"))
# Escrutinio.mostrar_resultados(Votante.VOTOS_TOTALES)
# Caso 1: Votante Válido
try:
    votante_ok = Votante("Elena", "Gómez", "46889241S", 35) # DNI VÁLIDO
    print(f"Creado OK: {votante_ok.dni}")
except ValueError as e:
    print(f"Error inesperado: {e}")

# Caso 2: Error de Letra (DNI con letra incorrecta)
try:
    votante_malo_letra = Votante("Félix", "López", "46889241X", 40) 
except ValueError as e:
    print(f"\nExcepción esperada (Letra incorrecta): {e}")

# Caso 3: Error de Longitud (DNI de 10 caracteres)
try:
    votante_malo_long = Votante("Sara", "Mata", "123456789A", 25)
except ValueError as e:
    print(f"\nExcepción esperada (Longitud incorrecta): {e}")