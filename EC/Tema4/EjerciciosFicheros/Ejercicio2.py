import csv
from pathlib import Path

BASE_DIR = Path(__file__).parent

fichero = Path(BASE_DIR / 'reporte_ventas.csv')

CABECERA = 'Region,Ventas_2024,Ventas_2025\n'
DATOS_NORTE = 'Norte,10500.50,12300.00\n'
DATOS_SUR = 'Sur,8900.25,9500.75\n'

with fichero.open('w', encoding='utf-8') as f:
    f.write(CABECERA + DATOS_NORTE + DATOS_SUR)