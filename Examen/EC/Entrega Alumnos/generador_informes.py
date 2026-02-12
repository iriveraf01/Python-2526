import json
import locale
from pathlib import Path
from datetime import datetime, date
from typing import Dict

from procesador import ProcesadorTemperaturas


class GeneradorInformes:
    @staticmethod
    def formatear_fecha_espanol(fecha:date)-> str:
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        return fecha.strftime("%A, %d de %B de %Y")
    
    def generar_informe_completo(self, procesador: ProcesadorTemperaturas, datos_api: dict) -> Path:
        fecha_hoy = datetime.now()
        print(fecha_hoy)
        BASE_DIR = Path(__file__).resolve().parent
        fichero = Path(BASE_DIR / f"informe_{fecha_hoy}.json")
        datos_a_guardar = {
            "fecha_generacion" : fecha_hoy.isoformat(),
            "fecha_generacion_legible" : self.formatear_fecha_espanol(fecha_hoy),
            "clima_actual": {
                "ciudad": datos_api['ciudad'],
                "temperatura": datos_api['temperatura_actual'],
                "sensacion_termica" : "hola",
                "descripcion" : datos_api['descripcion'],
                "humedad" : datos_api['humedad'],
                "timestamps" : fecha_hoy.isoformat(),
            },
        }
        with fichero.open('w', encoding='utf-8') as f:
            json.dump(datos_a_guardar, f, indent=4, ensure_ascii=False)
            print("Estadísticas guardadas correctamente.")

            print(f"\nDatos serializados y guardados con indentación en '{fichero.name}'.")

#PRUEBAS
if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent
    ruta_csv = BASE_DIR / "datos/temperaturas.csv"

    # Crear procesador y cargar datos del CSV
    procesador = ProcesadorTemperaturas(ruta_csv)
    procesador.cargar_desde_csv()

    # Probar generar informe con datos de API simulados
    datos_api_simulados = {
        "ciudad": "Madrid",
        "temperatura_actual": 18.5,
        "humedad": 62,
        "descripcion": "Parcialmente nublado"
    }

    generador = GeneradorInformes()
    ruta = generador.generar_informe_completo(procesador, datos_api_simulados)

    # Leer y mostrar el contenido del informe generado
    with ruta.open('r', encoding='utf-8') as f:
        contenido = json.load(f)
    print("\nContenido del informe:")
    print(json.dumps(contenido, indent=4, ensure_ascii=False))

    # Probar también con datos_api = None
    print("\n--- Prueba con datos_api = None ---")
    ruta2 = generador.generar_informe_completo(procesador, None)
    with ruta2.open('r', encoding='utf-8') as f:
        contenido2 = json.load(f)
    print("\nContenido del informe (sin API):")
    print(json.dumps(contenido2, indent=4, ensure_ascii=False))