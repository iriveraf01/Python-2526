import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from plantas import PlantaCreate, cargar_plantas, crear_planta, actualizar_planta, eliminar_planta

app = FastAPI(title="Agrosense API")

app.middleware(
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
    crear_planta(planta)
    return {"message": "Planta creada correctamente"}

@app.put("/plantas/{planta_id}")
def put_planta(planta_id: str, planta_data: PlantaCreate):
    actualizar_planta(planta_id, planta_data)
    return {"message": "Planta actualizada correctamente"}

@app.delete("/plantas/{planta_id}")
def delete_planta(planta):
    eliminar_planta(planta)
    return {"message": "Planta eliminada correctamente"}