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