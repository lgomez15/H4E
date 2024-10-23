# app/routers/asistencia.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.asistencia import AsistenciaCreate, AsistenciaRead, AsistenciaUpdate
from app.models.asistencia import Asistencia
from app.database.connection import get_db

router = APIRouter(
    prefix="/asistencia",
    tags=["Asistencia"],
)

@router.get("/", response_model=List[AsistenciaRead])
def listar_asistencias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Lista todas las asistencias con paginación.
    """
    asistencias = db.query(Asistencia).offset(skip).limit(limit).all()
    return asistencias

# Asistencias de un alumno
@router.get("/alumno/{alumno_id}", response_model=List[AsistenciaRead], responses={404: {"description": "No se encontraron asistencias para el alumno especificado"}})
def listar_asistencias_alumno(alumno_id: int, db: Session = Depends(get_db)):
    """
    Lista todas las asistencias de un alumno específico.
    """
    asistencias = db.query(Asistencia).filter(Asistencia.estudiante_id== alumno_id).all()
    if not asistencias:
        raise HTTPException(status_code=404, detail="No se encontraron asistencias para el alumno especificado")
    return asistencias

@router.get("/{asistencia_id}", response_model=AsistenciaRead, responses={404: {"description": "Asistencia no encontrada"}})
def obtener_asistencia(asistencia_id: int, db: Session = Depends(get_db)):
    """
    Obtiene una asistencia por su ID.
    """
    asistencia = db.query(Asistencia).filter(Asistencia.id == asistencia_id).first()
    if not asistencia:
        raise HTTPException(status_code=404, detail="Asistencia no encontrada")
    return asistencia

@router.post("/", response_model=AsistenciaRead, status_code=status.HTTP_201_CREATED, responses={201: {"description": "Asistencia creada exitosamente"}})
def registrar_asistencia(asistencia: AsistenciaCreate, db: Session = Depends(get_db)):
    """
    Registra una nueva asistencia.
    """
    db_asistencia = Asistencia(**asistencia.dict())
    db.add(db_asistencia)
    db.commit()
    db.refresh(db_asistencia)
    return db_asistencia

@router.put("/{asistencia_id}", response_model=AsistenciaRead, responses={404: {"description": "Asistencia no encontrada"}})
def actualizar_asistencia(asistencia_id: int, asistencia: AsistenciaUpdate, db: Session = Depends(get_db)):
    """
    Actualiza una asistencia existente.
    """
    db_asistencia = db.query(Asistencia).filter(Asistencia.id == asistencia_id).first()
    if not db_asistencia:
        raise HTTPException(status_code=404, detail="Asistencia no encontrada")
    for key, value in asistencia.dict(exclude_unset=True).items():
        setattr(db_asistencia, key, value)
    db.commit()
    db.refresh(db_asistencia)
    return db_asistencia

@router.delete("/{asistencia_id}", responses={204: {"description": "Asistencia eliminada correctamente"}, 404: {"description": "Asistencia no encontrada"}})
def eliminar_asistencia(asistencia_id: int, db: Session = Depends(get_db)):
    """
    Elimina una asistencia por su ID.
    """
    db_asistencia = db.query(Asistencia).filter(Asistencia.id == asistencia_id).first()
    if not db_asistencia:
        raise HTTPException(status_code=404, detail="Asistencia no encontrada")
    db.delete(db_asistencia)
    db.commit()
    return {"detail": "Asistencia eliminada correctamente"}


