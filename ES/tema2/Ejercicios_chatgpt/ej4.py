# 📝 Ejercicio: Uso combinado de deque, Counter y diccionarios
#       Se tiene una lista con accesos de usuarios a una aplicación (en orden de llegada):
# Paso 1
#   Utiliza un Counter para crear un diccionario llamado frecuencias que indique cuántas veces ha accedido cada usuario.
# Paso 2
#   A partir del diccionario frecuencias, crea una cola (deque) llamada cola_prioridad que contenga únicamente los usuarios que han accedido 2 o más veces.
#   (El orden debe ser el mismo en el que aparecen en frecuencias.items()).
# Paso 3
#   Simula la atención de usuarios:
#       Atiende (elimina) uno a uno los usuarios de cola_prioridad
#       Cada vez que se atienda un usuario, muéstralo por pantalla
# Paso 4
#   Crea un conjunto llamado usuarios_unicos con todos los usuarios distintos que aparecen en la lista accesos.
# Paso 5
#   Crea una tupla llamada resumen que contenga:
#       El número total de accesos
#       El número de usuarios únicos
#       El nombre del usuario con más accesos
#       (Pista: puedes usar most_common(1) de Counter).
from collections import Counter, deque
accesos = [
    "ana", "luis", "ana", "marta", "ana",
    "pedro", "luis", "luis", "marta"
]
# Paso 1
frecuencias = Counter(accesos)
print("Frecuencias:", frecuencias)
# Paso 2
cola_prioridad = deque()
for usuario, cuenta in frecuencias.items():
    if cuenta >= 2:
        cola_prioridad.append(usuario)
print("Cola de prioridad:", cola_prioridad)
# Paso 3 
while cola_prioridad:
    atendido = cola_prioridad.popleft()
    print("Atendiendo a:", atendido)  
# Paso 4
usuarios_unicos = set(accesos)
print("Usuarios únicos:", usuarios_unicos)
# Paso 5
total_accesos = len(accesos)
num_usuarios_unicos = len(usuarios_unicos)
usuario_mas_accesos = frecuencias.most_common(1)[0][0]
resumen = (total_accesos, num_usuarios_unicos, usuario_mas_accesos)
print("Resumen:", resumen)