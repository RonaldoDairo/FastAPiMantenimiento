# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from typing import List, ForwardRef

# app = FastAPI()

# class Temporada(BaseModel):
#     numero: int
#     episodios: List["Episodio"] = []  # Usamos la referencia ForwardRef

# class Episodio(BaseModel):
#     numero: int
#     titulo: str
#     fecha_emision: str
#     descripcion: str
#     actores: List[str] = []
#     director: str

# Temporada.update_forward_refs()  # Actualizamos las referencias adelantadas después de definir la clase Temporada

# class Serie(BaseModel):
#     nombre: str
#     genero: str
#     anio_lanzamiento: int
#     temporadas: List[Temporada] = []

# series_db = []

# @app.post("/series/", response_model=Serie)
# def crear_serie(serie: Serie):
#     series_db.append(serie)
#     return serie

# @app.get("/series/", response_model=List[Serie])
# def obtener_todas_las_series():
#     return series_db

# @app.get("/series/{serie_id}", response_model=Serie)
# def obtener_serie(serie_id: int):
#     try:
#         return series_db[serie_id - 1]
#     except IndexError:
#         raise HTTPException(status_code=404, detail="Serie no encontrada")

# @app.put("/series/{serie_id}", response_model=Serie)
# def actualizar_serie(serie_id: int, serie: Serie):
#     try:
#         series_db[serie_id - 1] = serie
#         return serie
#     except IndexError:
#         raise HTTPException(status_code=404, detail="Serie no encontrada")

# @app.delete("/series/{serie_id}", response_model=Serie)
# def eliminar_serie(serie_id: int):
#     try:
#         serie_eliminada = series_db.pop(serie_id - 1)
#         return serie_eliminada
#     except IndexError:
#         raise HTTPException(status_code=404, detail="Serie no encontrada")


from fastapi import FastAPI, HTTPException
from typing import List
from models import Serie
from database import series_db

app = FastAPI()

@app.post("/series/", response_model=Serie)
def crear_serie(serie: Serie):
    series_db.append(serie)
    return serie

@app.get("/series/", response_model=List[Serie])
def obtener_todas_las_series():
    return series_db

@app.get("/series/{serie_id}", response_model=Serie)
def obtener_serie(serie_id: int):
    try:
        return series_db[serie_id - 1]
    except IndexError:
        raise HTTPException(status_code=404, detail="Serie no encontrada")

@app.put("/series/{serie_id}", response_model=Serie)
def actualizar_serie(serie_id: int, serie: Serie):
    try:
        series_db[serie_id - 1] = serie
        return serie
    except IndexError:
        raise HTTPException(status_code=404, detail="Serie no encontrada")

@app.delete("/series/{serie_id}", response_model=Serie)
def eliminar_serie(serie_id: int):
    try:
        serie_eliminada = series_db.pop(serie_id - 1)
        return serie_eliminada
    except IndexError:
        raise HTTPException(status_code=404, detail="Serie no encontrada")