import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

fichero = Path(BASE_DIR / 'data/informes/2026/ventas') 

os.makedirs(fichero, exist_ok=True)

fichero_informe = fichero / "informe_final.txt"
print(fichero_informe)

fichero_informe.write_text("Informe creado", encoding="utf-8")