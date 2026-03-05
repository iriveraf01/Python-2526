# Ejercicio 1 – API de productos
# Crear una API completa con Pydantic para gestionar productos.
# Crea una clase llamada CrearProducto con Pydantic con métodos:
# - nombre: tipo cadena, obligatorio, mínima longitud 3 y máxima 100, descripción:
# Nombre del producto.
# - precio: tipo float, obligatorio, mayor que cero y descripción: Precio en euros(debe ser
# positivo).
# - descripción: tipo cadena opcional.
# - categorías: lista de cadenas, por defecto vacía y descripción: “Lista de categorías”.
# - stock: tipo entero, por defecto cero y mayor o igual que cero, descripción: “Cantidad
# en stock”.
# Haz un validador de precio que si no tiene 2 decimales raise ValueError con el mensaje
# “El nombre no puede contener números”
# Otro validador del nombre, que compruebe que todo es texto, si no raise ValueError con
# el mensaje “El nombre no puede contener números”.
from pydantic import BaseModel, Field, field_validator, ConfigDict
from datetime import datetime, date, time, timedelta
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
class CrearProducto(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100, description="Nombre del producto")
    precio: float = Field(..., gt=0, description="Precio en euros (debe ser positivo)")
    descripcion: str = Field(None, description="Descripción del producto")
    categorias: list[str] = Field(default_factory=list, description="Lista de categorías")
    stock: int = Field(0, ge=0, description="Cantidad en stock")

    @field_validator("precio")
    @classmethod
    def precio_dos_decimales(cls, valor):
        if round(valor, 2) != valor:
            raise ValueError('El precio solo puede tener 2 decimales')
        return valor

    @field_validator('nombre')
    @classmethod
    def nombre_sin_numeros(cls, valor):
        if any(c.isdigit() for c in valor):
            raise ValueError('El nombre no puede contener números')
        return valor.strip() # puede transformar: elimina espacios
    
# Crear una clase Producto con Pydantic, que incluirá id y fecha_creación de tipo
# datetime.
class Producto(BaseModel):
    # Añadele una clase Config con json_schema_extra para mostrar en la documentación un
    # ejemplo.
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "nombre": "Camiseta",
                "precio": 19.99,
                "descripcion": "Camiseta de algodón",
                "categorias": ["Ropa", "Hombre"],
                "stock": 100,
                "fecha_creacion": "2024-06-01T12:00:00"
            }
        }
    )
    id: int
    nombre: str
    precio: float
    descripcion: str | None
    categorias: list[str]
    stock: int
    fecha_creacion: datetime
# Creamos una BD simulada:
productos_db: list[Producto] = [
    Producto(
        id=1,
        nombre="Camiseta Básica",
        precio=19.99,
        descripcion="Camiseta de algodón 100% unisex",
        categorias=["Ropa", "Unisex"],
        stock=50,
        fecha_creacion=datetime(2024, 6, 1, 12, 0, 0)
    )
]
siguiente_id = 2 
# - Crea el endpoint tipo POST de /productos, con response_model “Producto”.
# Tendrá un método crearProducto con parámetro de entrada un producto de tipo
# CrearProducto. Crea un nuevo producto y añadelo a productos_db, suma 1 a
# siguiente_id y retorna el nuevo producto.
app = FastAPI(
    title="API de Productos hecho por mí",
    description="API para gestionar productos con FastAPI y Pydantic",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/productos", response_model=Producto)
def crear_producto(producto: CrearProducto):
    global siguiente_id
    nuevo_producto = Producto(
        id=siguiente_id,
        nombre=producto.nombre,
        precio=producto.precio,
        descripcion=producto.descripcion,
        categorias=producto.categorias,
        stock=producto.stock,
        fecha_creacion=datetime.now()
    )
    productos_db.append(nuevo_producto)
    siguiente_id += 1
    return nuevo_producto
# - Crea el endpoint tipo GET de /productos con response_model List[Producto] que
# tendrá el método listar_productos que retorne productos_db.
@app.get("/productos", response_model=list[Producto])
def listar_productos():
    return productos_db
# - Crear el endpoint tipo GET de /productos/idProducto con respondse_model
# “Producto”.
# Tendrá un método obtener_producto(con id del producto de tipo int de entrada), que
# recorre todo “productos_db” y cuando coincida con el id de producto pasado por
# parámetro, lo devuelva.
@app.get("/productos/{id_producto}", response_model=Producto)
def obtener_producto(id_producto: int):
    for producto in productos_db:
        if producto.id == id_producto:
            return producto
    return {"error": "Producto no encontrado"}

@app.get("/")
async def root():
    return {
        "mensaje": "API de Productos funcionando correctamente",
        "version": "1.0.0",
        "endpoints": {
            "crear_producto": "/productos (POST)",
            "listar_productos": "/productos (GET)",
            "obtener_producto": "/productos/{id_producto} (GET)"
        }
    }

if __name__ == "__main__":
    uvicorn.run("ej1api:app", host="127.0.0.1", port=8001)