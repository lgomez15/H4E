# app/routers/estudiantes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.estudiante import EstudianteCreate, EstudianteRead, EstudianteUpdate
from app.schemas.calificacion import CalificacionRead  # Importar aquí
from app.models.estudiante import Estudiante
from app.models.calificacion import Calificacion
from app.database.connection import get_db
from app.schemas.datos_contextuales import DatosContextualesRead
from app.models.datos_contextuales import DatosContextuales



router = APIRouter(
    prefix="/estudiantes",
    tags=["Estudiantes"],
)

@router.get("/", response_model=List[EstudianteRead])
def listar_estudiantes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    estudiantes = db.query(Estudiante).offset(skip).limit(limit).all()
    return estudiantes

@router.get("/{estudiante_id}", response_model=EstudianteRead)
def obtener_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    estudiante = db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return estudiante

@router.post("/", response_model=EstudianteRead)
def crear_estudiante(estudiante: EstudianteCreate, db: Session = Depends(get_db)):
    db_estudiante = Estudiante(**estudiante.dict())
    db.add(db_estudiante)
    db.commit()
    db.refresh(db_estudiante)
    return db_estudiante

@router.put("/{estudiante_id}", response_model=EstudianteRead)
def actualizar_estudiante(estudiante_id: int, estudiante: EstudianteUpdate, db: Session = Depends(get_db)):
    db_estudiante = db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()
    if not db_estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    for key, value in estudiante.dict(exclude_unset=True).items():
        setattr(db_estudiante, key, value)
    db.commit()
    db.refresh(db_estudiante)
    return db_estudiante

@router.delete("/{estudiante_id}")
def eliminar_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    db_estudiante = db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()
    if not db_estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    db.delete(db_estudiante)
    db.commit()
    return {"detail": "Estudiante eliminado correctamente"}

@router.get("/datos-contextuales/{estudiante_id}", response_model=DatosContextualesRead)
def obtener_datos_contextuales(estudiante_id: int, db: Session = Depends(get_db)):
    datos = db.query(DatosContextuales).filter(DatosContextuales.estudiante_id == estudiante_id).first()
    if datos is None:
        raise HTTPException(status_code=404, detail="Datos contextuales no encontrados para este estudiante")
    return datos

@router.get("/{estudiante_id}/calificaciones", response_model=List[CalificacionRead])
def obtener_calificaciones_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    estudiante = db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    calificaciones = db.query(Calificacion).filter(Calificacion.estudiante_id == estudiante_id).all()
    return calificaciones