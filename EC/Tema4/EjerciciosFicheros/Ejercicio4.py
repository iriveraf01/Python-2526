from pathlib import Path
import csv

BASE_DIR = Path(__file__).parent
fichero = Path(BASE_DIR / "log_acceso.txt")

fichero.write_text("""[2024-11-20 10:05:01] ERROR: Fichero no encontrado en /data/a/fichero.txt
[2024-11-20 10:05:30] INFO: Usuario 'user_001' ha iniciado sesion.
[2024-11-20 10:06:15] WARN: Disco al 80%.
[2024-11-20 10:06:40] INFO: Usuario 'user_002' ha iniciado sesion.
[2024-11-20 10:07:05] ERROR: Conexión perdida con base de datos.""")

with fichero.open('r', encoding='utf-8') as f:
    lector = csv.reader(f)

    for fila in lector:
        if 'ERROR' in fila[0] or 'WARN' in fila[0]:
            print(fila[0])
            fichero_errores = Path(BASE_DIR / "log_errores.txt")
            with fichero_errores.open('a', encoding='utf-8') as f:
                f.write(fila[0] + '\n')
