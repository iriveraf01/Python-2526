# Ejercicio 1
# Define una lista de diccionarios, donde cada diccionario representa una tarea con las
# claves título, estado (True/False) y prioridad (número). Serializa esta lista y guárdala en
# un fichero llamado tareas.json. Asegúrate de usar indent=2 para que el JSON sea
# legible.
# Estructura de la lista:
# tareas = [
#  {'titulo': 'Revisar tema JSON', 'estado': True, 'prioridad': 1},
#  # ... otras tareas
# ]

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
fichero = Path(BASE_DIR / 'tareas.json')

tareas = [
    {'titulo': 'Revisar tema JSON', 'estado': True, 'prioridad': 1},
    {'titulo': 'Hacer la compra', 'estado': False, 'prioridad': 2},
    {'titulo': 'Llamar al medico', 'estado': False, 'prioridad': 1},
    {'titulo': 'Estudiar para el examen', 'estado': True, 'prioridad': 3}
]

with fichero.open('w', encoding='utf-8') as f:
    json.dump(tareas, f, indent=2)
    print("Fichero creado con las tareas")