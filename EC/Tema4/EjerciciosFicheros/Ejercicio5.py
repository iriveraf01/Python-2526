import csv
from pathlib import Path

BASE_DIR = Path(__file__).parent

fichero = Path(BASE_DIR / 'empleados.csv') 

with fichero.open('r', encoding='utf-8') as f:
    lector = csv.DictReader(f)
    total_ventas = 0
    for i in lector:
        if i['Departamento'] == "Ventas":
            total_ventas += int(i['Salario'])
    print(f"Total ventas {total_ventas}€")