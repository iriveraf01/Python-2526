# Ejercicio 2
# Escribe un programa que:
# - Cargue el fichero tareas.json del ejercicio anterior.
# - Cuente cuántas tareas tienen el estado igual a False (tareas pendientes).
# - Muestre los títulos de las tareas pendientes.
# - Añada una nueva tarea a la lista ('titulo': 'Planificar examen', 'estado': False, 'prioridad':
# 3).
# - Sobrescriba el fichero tareas.json con la lista actualizada.
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
fichero = Path(BASE_DIR / 'tareas.json')

try:
    # Cargar el fichero
    with fichero.open('r', encoding='utf-8') as f:
        datos_cargados = json.load(f)
    # Cuenta cuántas tareas tienen el estado False
    tareas_pendientes = [tarea for tarea in datos_cargados if not tarea['estado']]
    print(f"Número de tareas pendientes: {len(tareas_pendientes)}")
    # Muestra los títulos pendientes
    print("Títulos de las tareas pendientes:")
    for tarea in tareas_pendientes:
        print(f"- {tarea['titulo']}")
    # Añado nueva tarea
    nueva_tarea = {'titulo': 'Planificar examen', 'estado': False, 'prioridad': 3}
    datos_cargados.append(nueva_tarea)

    with fichero.open('w', encoding='utf-8') as f:
        json.dump(datos_cargados, f, indent=2)
        print("Fichero actualizado con la nueva tarea.")

except FileNotFoundError:
    print(f"Error: No se encontró el fichero {fichero.name}.")

except json.JSONDecodeError:
    # Esta excepción es clave: el fichero existe, pero el contenido es JSON inválido.
    print(f"Error: El fichero {fichero.name} contiene JSON inválido.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")