from pydantic import BaseModel
from typing import List, ForwardRef

Temporada = ForwardRef("Temporada")

class Episodio(BaseModel):
    numero: int
    titulo: str
    fecha_emision: str
    descripcion: str
    actores: List[str] = []
    director: str

class Temporada(BaseModel):
    numero: int
    episodios: List[Episodio] = []

Temporada.update_forward_refs()

class Serie(BaseModel):
    nombre: str
    genero: str
    anio_lanzamiento: int
    temporadas: List[Temporada] = []