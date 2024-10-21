from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.calificacion import CalificacionCreate, CalificacionRead, CalificacionUpdate
from app.models.calificacion import Calificacion
from app.database.connection import get_db

router = APIRouter(
    prefix="/calificaciones",
    tags=["Calificaciones"],
)

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
