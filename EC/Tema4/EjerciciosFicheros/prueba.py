import csv
from pathlib import Path

BASE_DIR = Path(__file__).parent

fichero = Path(BASE_DIR / 'datos.csv')

with fichero.open('r', encoding='utf-8') as f:
    lector = csv.DictReader(f)
    for i in lector:
        print(i)