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
from pydantic import BaseModel, Field, field_validator
from datetime import datetime, date, time, timedelta
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
    id : int
    fecha_creacion: datetime
# Añadele una clase Config con json_schema_extra para mostrar en la documentación un
# ejemplo.
# Creamos una BD simulada:
# productos_db: List[Producto] = []
# siguiente_id = 1
# - Crea el endpoint tipo POST de /productos, con response_model “Producto”.
# Tendrá un método crearProducto con parámetro de entrada un producto de tipo
# CrearProducto. Crea un nuevo producto y añadelo a productos_db, suma 1 a
# siguiente_id y retorna el nuevo producto.
# - Crea el endpoint tipo GET de /productos con response_model List[Producto] que
# tendrá el método listar_productos que retorne productos_db.
# - Crear el endpoint tipo GET de /productos/idProducto con respondse_model
# “Producto”.
# Tendrá un método obtener_producto(con id del producto de tipo int de entrada), que
# recorre todo “productos_db” y cuando coincida con el id de producto pasado por
# parámetro, lo devuelva.