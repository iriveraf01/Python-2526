import csv
from pathlib import Path

BASE_DIR = Path(__file__).parent

fichero = Path(BASE_DIR / 'reporte_ventas.csv') 

with fichero.open('r', encoding='utf-8') as f:
    lector = csv.reader(f)
    next(lector)  # Salta la cabecera (Region,Ventas_2024,Ventas_2025)
    suma_total = 0
    for fila in lector:
        suma_total += float(fila[2])  

with fichero.open('a', encoding='utf-8') as f:
    f.write(f'Total,0,{suma_total}\n')