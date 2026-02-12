from pathlib import Path
from typing import List
import csv
import locale
from pydantic import ValidationError

from modelos import RegistroTemperatura

class ProcesadorTemperaturas: 
    total_procesados:int = 0
    def __init__(self, ruta_datos:Path = "datos/temperaturas.csv", registros: List[RegistroTemperatura] = []):
        self.ruta_datos = ruta_datos
        self.registros = []
    
    def cargar_desde_csv(self) -> None:
        fichero = self.ruta_datos
        try:
            with fichero.open('r', newline='', encoding='utf-8') as f:
                # La cabecera se usa como clave automáticamente
                lector = csv.DictReader(f)

                for fila in lector:
                    convertido = RegistroTemperatura.desde_dict(fila)
                    self.registros.append(convertido)
                print(f"Cargados {len(self.registros)} registros desde {fichero.name}")

                for registro in self.registros:
                    print(registro)
            
        except FileNotFoundError:
            print(f"Error: El archivo '{fichero.name}' no existe")
        except ValidationError:
            print(f"Error: en fila X del {fichero.name}, esta fila será omitida")

    def calcular_estadisticas(self) -> dict:
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        if not self.registros:
            return None
        # return {
        #     "temperatura_maxima_absoluta":
        # }
    
    def mostrar_total_procesados(cls) -> None:
        return f"Total de registros procesados por todas las instancias: {cls.total_procesados}"
#PRUEBAS  
if __name__ == "__main__":
    # Ejemplo de uso
    BASE_DIR = Path(__file__).resolve().parent
    ruta_csv = Path(BASE_DIR / "datos/temperaturas.csv")
    procesador = ProcesadorTemperaturas(ruta_csv)
    
    try:
        procesador.cargar_desde_csv()
        # estadisticas = procesador.calcular_estadisticas()
        # print("\nEstadísticas calculadas:")
        # for clave, valor in estadisticas.items():
        #     print(f"{clave}: {valor}")
        
        # ProcesadorTemperaturas.mostrar_total_procesados()
    
    except FileNotFoundError as e:
        print(e)