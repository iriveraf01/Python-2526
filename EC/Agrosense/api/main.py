import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from plantas import (
    PlantaCreate,
    cargar_plantas,
    crear_planta,
    actualizar_planta,
    eliminar_planta,
)

app = FastAPI(title="Agrosense API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/plantas")
def get_plantas():
    plantas = cargar_plantas()
    return list(p.model_dump() for p in plantas.values())

@app.post("/plantas")
def post_planta(planta: PlantaCreate):
    nueva_planta = crear_planta(planta)

    if nueva_planta is None:
        raise HTTPException(
            status_code=409,
            detail=f"La planta '{planta.nombre}' ya existe en tu colección."
        )

    return nueva_planta

@app.put("/plantas/{planta_id}")
def put_planta(planta_id: str, planta_data: PlantaCreate):
    plantas = cargar_plantas()

    if planta_id not in plantas:
        raise HTTPException(
            status_code=404,
            detail="Planta no encontrada"
        )

    actualizar_planta(planta_id, planta_data)
    return {"message": "Planta actualizada correctamente"}

@app.delete("/plantas/{planta_id}")
def delete_planta(planta_id: str):
    plantas = cargar_plantas()

    if planta_id not in plantas:
        raise HTTPException(
            status_code=404,
            detail="Planta no encontrada"
        )

    eliminar_planta(planta_id)
    return {"message": "Planta eliminada correctamente"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001)