from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.estudiante import EstudianteCreate, EstudianteRead, EstudianteUpdate
from app.models.estudiante import Estudiante
from app.database.connection import get_db

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

@router.get("/clase/{clase_id}", response_model=List[EstudianteRead])
def obtener_estudiantes_por_clase(clase_id: int, db: Session = Depends(get_db)):
    estudiantes = db.query(Estudiante).filter(Estudiante.clase_id == clase_id).all()
    if not estudiantes:
        # Verificar si la clase existe
        clase = db.query(Clase).filter(Clase.id == clase_id).first()
        if not clase:
            raise HTTPException(status_code=404, detail="Clase no encontrada")
        else:
            return []  # La clase existe pero no tiene estudiantes
    return estudiantes