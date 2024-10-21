# app/routers/asistencia.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.asistencia import AsistenciaCreate, AsistenciaRead, AsistenciaUpdate
from app.models.asistencia import Asistencia
from app.database.connection import get_db

router = APIRouter(
    prefix="/asistencia",
    tags=["Asistencia"],
)

# Define your endpoints here


@router.get("/", response_model=List[AsistenciaRead])
def listar_asistencias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    asistencias = db.query(Asistencia).offset(skip).limit(limit).all()
    return asistencias

@router.get("/{asistencia_id}", response_model=AsistenciaRead)
def obtener_asistencia(asistencia_id: int, db: Session = Depends(get_db)):
    asistencia = db.query(Asistencia).filter(Asistencia.id == asistencia_id).first()
    if not asistencia:
        raise HTTPException(status_code=404, detail="Asistencia no encontrada")
    return asistencia

@router.post("/", response_model=AsistenciaRead)
def registrar_asistencia(asistencia: AsistenciaCreate, db: Session = Depends(get_db)):
    db_asistencia = Asistencia(**asistencia.dict())
    db.add(db_asistencia)
    db.commit()
    db.refresh(db_asistencia)
    return db_asistencia

@router.put("/{asistencia_id}", response_model=AsistenciaRead)
def actualizar_asistencia(asistencia_id: int, asistencia: AsistenciaUpdate, db: Session = Depends(get_db)):
    db_asistencia = db.query(Asistencia).filter(Asistencia.id == asistencia_id).first()
    if not db_asistencia:
        raise HTTPException(status_code=404, detail="Asistencia no encontrada")
    for key, value in asistencia.dict(exclude_unset=True).items():
        setattr(db_asistencia, key, value)
    db.commit()
    db.refresh(db_asistencia)
    return db_asistencia

@router.delete("/{asistencia_id}")
def eliminar_asistencia(asistencia_id: int, db: Session = Depends(get_db)):
    db_asistencia = db.query(Asistencia).filter(Asistencia.id == asistencia_id).first()
    if not db_asistencia:
        raise HTTPException(status_code=404, detail="Asistencia no encontrada")
    db.delete(db_asistencia)
    db.commit()
    return {"detail": "Asistencia eliminada correctamente"}
