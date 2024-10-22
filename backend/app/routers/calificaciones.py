from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func  # Importar func para operaciones agregadas
from typing import List
from pydantic import BaseModel  # Importar BaseModel
from app.schemas.calificacion import CalificacionCreate, CalificacionRead, CalificacionUpdate
from app.models.calificacion import Calificacion
from app.database.connection import get_db

router = APIRouter(
    prefix="/calificaciones",
    tags=["Calificaciones"],
)

# 1. Definir el modelo de respuesta **antes** de usarlo en el decorador
class DetalleCalificacion(BaseModel):
    examen: str
    nota_estudiante: float
    media_examen: float

    class Config:
        from_attributes = True  # Reemplaza 'orm_mode' con 'from_attributes' en Pydantic V2

# 2. Rutas específicas primero

# Media de calificaciones para un alumno
@router.get("/media/{alumno_id}", response_model=float)
def media_calificaciones_alumno(alumno_id: int, db: Session = Depends(get_db)):
    calificaciones = db.query(Calificacion).filter(Calificacion.estudiante_id == alumno_id).all()
    if not calificaciones:
        raise HTTPException(status_code=404, detail="Calificaciones no encontradas")
    return sum([calificacion.nota for calificacion in calificaciones]) / len(calificaciones)

# Media de calificaciones de todos los alumnos
@router.get("/media", response_model=float)
def media_calificaciones(db: Session = Depends(get_db)):
    calificaciones = db.query(Calificacion).all()
    if not calificaciones:
        raise HTTPException(status_code=404, detail="Calificaciones no encontradas")
    return sum([calificacion.nota for calificacion in calificaciones]) / len(calificaciones)

# 3. Rutas genéricas después
@router.get("/", response_model=List[CalificacionRead])
def listar_calificaciones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    calificaciones = db.query(Calificacion).offset(skip).limit(limit).all()
    return calificaciones

@router.get("/{calificacion_id}", response_model=CalificacionRead)
def obtener_calificacion(calificacion_id: int, db: Session = Depends(get_db)):
    calificacion = db.query(Calificacion).filter(Calificacion.id == calificacion_id).first()
    if not calificacion:
        raise HTTPException(status_code=404, detail="Calificación no encontrada")
    return calificacion

@router.post("/", response_model=CalificacionRead)
def crear_calificacion(calificacion: CalificacionCreate, db: Session = Depends(get_db)):
    db_calificacion = Calificacion(**calificacion.dict())
    db.add(db_calificacion)
    db.commit()
    db.refresh(db_calificacion)
    return db_calificacion

@router.put("/{calificacion_id}", response_model=CalificacionRead)
def actualizar_calificacion(calificacion_id: int, calificacion: CalificacionUpdate, db: Session = Depends(get_db)):
    db_calificacion = db.query(Calificacion).filter(Calificacion.id == calificacion_id).first()
    if not db_calificacion:
        raise HTTPException(status_code=404, detail="Calificación no encontrada")
    for key, value in calificacion.dict(exclude_unset=True).items():
        setattr(db_calificacion, key, value)
    db.commit()
    db.refresh(db_calificacion)
    return db_calificacion

@router.delete("/{calificacion_id}")
def eliminar_calificacion(calificacion_id: int, db: Session = Depends(get_db)):
    db_calificacion = db.query(Calificacion).filter(Calificacion.id == calificacion_id).first()
    if not db_calificacion:
        raise HTTPException(status_code=404, detail="Calificación no encontrada")
    db.delete(db_calificacion)
    db.commit()
    return {"detail": "Calificación eliminada correctamente"}

# 4. Rutas adicionales

# Todas las calificaciones de un alumno
@router.get("/alumno/{alumno_id}", response_model=List[CalificacionRead])
def listar_calificaciones_alumno(alumno_id: int, db: Session = Depends(get_db)):
    calificaciones = db.query(Calificacion).filter(Calificacion.estudiante_id == alumno_id).all()
    if not calificaciones:
        raise HTTPException(status_code=404, detail="Calificaciones no encontradas")
    return calificaciones

# Nuevo endpoint para obtener detalle de calificaciones de un estudiante
@router.get("/detalle/{estudiante_id}", response_model=List[DetalleCalificacion])
def detalle_calificaciones(estudiante_id: int, db: Session = Depends(get_db)):
    # Obtener todas las calificaciones del estudiante
    calificaciones_estudiante = db.query(Calificacion).filter(Calificacion.estudiante_id == estudiante_id).all()
    
    if not calificaciones_estudiante:
        raise HTTPException(status_code=404, detail="Calificaciones del estudiante no encontradas")
    
    # Optimización: Obtener todas las medias de los exámenes en una sola consulta
    examenes = [calificacion.examen for calificacion in calificaciones_estudiante]
    medias = db.query(
        Calificacion.examen,
        func.avg(Calificacion.nota).label("media_examen")
    ).filter(Calificacion.examen.in_(examenes)).group_by(Calificacion.examen).all()
    
    # Crear un diccionario para acceder rápidamente a las medias
    medias_dict = {examen: round(media, 2) for examen, media in medias}
    
    resultado = []
    
    for calificacion in calificaciones_estudiante:
        media_examen = medias_dict.get(calificacion.examen)
        resultado.append({
            "examen": calificacion.examen,
            "nota_estudiante": calificacion.nota,
            "media_examen": media_examen
        })
    
    return resultado
