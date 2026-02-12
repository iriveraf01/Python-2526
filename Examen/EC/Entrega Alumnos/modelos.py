from datetime import date
from pydantic import BaseModel, Field


class RegistroTemperatura(BaseModel):
    fecha: date
    temperatura_max: float = Field(ge=-100, le=60)
    temperatura_min: float = Field(ge=-100, le=60)
    ciudad: str

    @classmethod
    def desde_dict(cls, datos:dict):
        if isinstance(datos['fecha'], str):
            datos['fecha'] = date.fromisoformat(datos['fecha'])
        datos = {
            'fecha'  : datos['fecha'],
            'temperatura_max' : float(datos['temperatura_max']),
            'temperatura_min' : float(datos['temperatura_min']),
            'ciudad' : datos['ciudad']
        }
        
        return cls(**datos)
    
    def __str__(self):
        return f"[{self.fecha}] {self.ciudad}: {self.temperatura_min} - {self.temperatura_max}"


#PRUEBAS
if __name__ == "__main__":
    # Ejemplo de uso
    datos_ejemplo = {
        "fecha": "2026-06-01",
        "temperatura_max": "30.5",
        "temperatura_min": "20.0",
        "ciudad": "Madrid"
    }
    
    registro = RegistroTemperatura.desde_dict(datos_ejemplo)
    print(registro)