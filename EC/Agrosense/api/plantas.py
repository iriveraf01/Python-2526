import json
from pydantic import BaseModel
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / 'data'
DATA_DIR.mkdir(exist_ok=True)

PLANTAS_FILE = DATA_DIR / "plantas.json"


class PlantaCreate(BaseModel):
    
    nombre: str
    nombre_cientifico: Optional[str] = ""
    descripcion: Optional[str] = ""
    recinto_id: Optional[str] = None
    cantidad: int = 1
    imagen_url: Optional[str] = ""
    fecha_adquisicion: Optional[str] = None
    ultimo_riego: Optional[str] = None
    necesita_trasplante: bool = False
    notas: Optional[str] = ""
class Planta(PlantaCreate):
    id: str
    created_at: str = datetime.now().isoformat()
    updated_at: str = datetime.now().isoformat()


def crear_planta(planta: PlantaCreate):
    
    """Crea una nueva planta"""
    
    plantas = cargar_plantas()
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    nombre_planta = planta.nombre.lower()
    planta_id = f"{nombre_planta.replace(" ", "_")}_{timestamp}"
    
    for p in plantas.values():
        if p.nombre.lower() == nombre_planta:
            print(f"La planta con nombre {planta.nombre} ya existe.")
            return
    
    nueva_planta = Planta(
        id = planta_id,
        nombre = planta.nombre,
        nombre_cientifico = planta.nombre_cientifico,
        descripcion = planta.descripcion,
        recinto_id = planta.recinto_id,
        cantidad = planta.cantidad,
        imagen_url = planta.imagen_url,
        fecha_adquisicion = planta.fecha_adquisicion,
        ultimo_riego = planta.ultimo_riego,
        necesita_trasplante = planta.necesita_trasplante,
        notas = planta.notas
    )
    
    plantas[planta_id] = nueva_planta
    guardar_plantas(plantas)
    print("Planta creada correctamente")

def cargar_plantas() -> Dict[str, Planta]:
    """Veo mi archivo de plantas, si hay algo devuelvo el contenido del mismo"""
    if not PLANTAS_FILE.exists():
        return {}

    with PLANTAS_FILE.open( "r", encoding="utf-8") as f:
        data = json.load(f)
        return {k: Planta(**v) for k,v in data.items()}

def guardar_plantas(plantas: Dict[str, Planta]):
    """Recibo una lista de plantas y las guardo en el archivo de plantas"""
    with PLANTAS_FILE.open( "w", encoding="utf-8") as f:
        data = {k: v.model_dump() for k,v in plantas.items()}
        json.dump(data, f, indent=4, ensure_ascii=False)

def actualizar_planta(planta_id: str, planta_data: PlantaCreate):
    """Actualiza una planta existente"""
    plantas = cargar_plantas()
    if planta_id not in plantas:
        print(f"La planta con ID {planta_id} no existe.")
        return
    planta_existente = plantas[planta_id]

    planta_actualizada = Planta(
        id=planta_id,
        nombre=planta_data.nombre,
        nombre_cientifico=planta_data.nombre_cientifico,
        descripcion=planta_data.descripcion,
        recinto_id=planta_data.recinto_id,
        cantidad=planta_data.cantidad,
        imagen_url=planta_data.imagen_url,
        fecha_adquisicion=planta_data.fecha_adquisicion,
        ultimo_riego=planta_data.ultimo_riego,
        necesita_trasplante=planta_data.necesita_trasplante,
        notas=planta_data.notas,
        created_at=planta_existente.created_at,
        updated_at=datetime.now().isoformat()
    )
    plantas[planta_id] = planta_actualizada
    guardar_plantas(plantas)
    print("Planta modificada correctamente")

def eliminar_planta(planta_id: str):
    """Elimina una planta existente"""
    plantas = cargar_plantas()
    if planta_id not in plantas:
        print(f"La planta con ID {planta_id} no existe.")
        return
    del plantas[planta_id]
    guardar_plantas(plantas)
    print("Planta eliminada correctamente")

def main():
    nueva_planta_test = PlantaCreate(
        nombre="Monstera Deliciosa",
        nombre_cientifico="Monstera deliciosa",
        descripcion="Planta tropical con hojas grandes y agujereadas.",
        recinto_id="salon_principal", # ID de ejemplo
        cantidad=1,
        imagen_url="https://ejemplo.com/monstera.jpg",
        fecha_adquisicion="2024-05-15",
        ultimo_riego="2024-05-20",
        necesita_trasplante=False,
        notas="Le gusta la luz indirecta y mucha humedad."
    )
    # Ejecución de la prueba
    crear_planta(nueva_planta_test)
    planta_modificada = PlantaCreate(
        nombre="Cactus Deliciosa",
        nombre_cientifico="Cactus deliciosa",
        descripcion="Planta tropical con hojas grandes y agujereadas.",
        recinto_id="salon_principal", # ID de ejemplo
        cantidad=1,
        imagen_url="https://ejemplo.com/cactus.jpg",
        fecha_adquisicion="2024-05-17",
        ultimo_riego="2024-05-20",
        necesita_trasplante=False,
        notas="Le gusta la luz indirecta y mucha humedad."
    )

    actualizar_planta("monstera_deliciosa_20260122184431", planta_modificada)
    eliminar_planta("monstera_deliciosa_20260122184431")
    
if __name__ == "__main__":
    main()
    
