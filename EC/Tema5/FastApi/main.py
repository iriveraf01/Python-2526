from fastapi import FastAPI
# Crear la aplicación FastAPI
app = FastAPI()
# Definir una ruta (endpoint)
@app.get("/")
def root():
 """Ruta raíz - Responde a GET /"""
 return {"mensaje": "¡Hola desde FastAPI!"}
# Otra ruta
@app.get("/saludo/{nombre}")
def saludar(nombre: str):
 """Ruta con parámetro en la URL"""
 return {"mensaje": f"Hola, {nombre}!"}

if __name__ == "__main__":
 import uvicorn
 uvicorn.run("main:app", host="0.0.0.0", port=8000)