import requests
import json
from pathlib import Path

URL_API = "http://16.171.21.119:8000/alumnos"

def obtener_alumnos():
    response = requests.get(URL_API)
    response.raise_for_status()  # Lanza error si falla la petición
    return response.json()

def main():
    datos = obtener_alumnos()
    alumnos = datos["alumnos"]
    print(f"Se han obtenido {len(alumnos)} alumnos.\n")

    print("--- Estadísticas por alumno ---")

    estadisticas_alumnos = []
    for alumno in alumnos:
        nota_media = round((alumno['nota1'] + alumno['nota2']) / 2 , 2)
        print(f"{alumno['nombre']} {alumno['apellidos']}: nota media = {nota_media}")
        estadisticas_alumnos.append({
            "nombre": alumno['nombre'],
            "apellidos": alumno['apellidos'],
            "nota_media": nota_media
        })
    
    print("\n--- Estadísticas por curso ---")
    cursos = {}
    for alumno in alumnos:
        curso = alumno['curso']
        nota_media = round((alumno['nota1'] + alumno['nota2']) / 2 , 2)
        if curso not in cursos:
            cursos[curso] = []
        cursos[curso].append(nota_media)
    
    estadisticas_curso = []
    for curso, valor in cursos.items():
        num_alumnos = len(valor)
        nota_media_curso = round(sum(valor) / num_alumnos, 2)
        print(f"{curso}: nota media = {nota_media_curso} ({num_alumnos} alumnos)")
        estadisticas_curso.append({
            "curso" : curso,
            "nota_media_curso": nota_media_curso,
            "num_alumnos": num_alumnos
        })

    resultado = {
        "estadisticas_alumnos": estadisticas_alumnos,
        "estadisticas_cursos": estadisticas_curso
    }

    BASE_DIR = Path(__file__).resolve().parent
    fichero = Path(BASE_DIR / 'estadisticas.json')

    with fichero.open('w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=4, ensure_ascii=False)
        print("Estadísticas guardadas correctamente.")

if __name__ == "__main__":
    main()
