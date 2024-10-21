from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.profesor import ProfesorCreate, ProfesorRead, ProfesorUpdate
from app.models.profesor import Profesor
from app.database.connection import get_db

router = APIRouter(
    prefix="/profesores",
    tags=["Profesores"],
)

@router.get("/", response_model=List[ProfesorRead])
def listar_profesores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    profesores = db.query(Profesor).offset(skip).limit(limit).all()
    return profesores

@router.get("/{profesor_id}", response_model=ProfesorRead)
def obtener_profesor(profesor_id: int, db: Session = Depends(get_db)):
    profesor = db.query(Profesor).filter(Profesor.id == profesor_id).first()
    if not profesor:
        raise HTTPException(status_code=404, detail="Profesor no encontrado")
    return profesor

@router.post("/", response_model=ProfesorRead)
def crear_profesor(profesor: ProfesorCreate, db: Session = Depends(get_db)):
    db_profesor = Profesor(**profesor.dict())
    db.add(db_profesor)
    db.commit()
    db.refresh(db_profesor)
    return db_profesor

@router.put("/{profesor_id}", response_model=ProfesorRead)
def actualizar_profesor(profesor_id: int, profesor: ProfesorUpdate, db: Session = Depends(get_db)):
    db_profesor = db.query(Profesor).filter(Profesor.id == profesor_id).first()
    if not db_profesor:
        raise HTTPException(status_code=404, detail="Profesor no encontrado")
    for key, value in profesor.dict(exclude_unset=True).items():
        setattr(db_profesor, key, value)
    db.commit()
    db.refresh(db_profesor)
    return db_profesor

@router.delete("/{profesor_id}")
def eliminar_profesor(profesor_id: int, db: Session = Depends(get_db)):
    db_profesor = db.query(Profesor).filter(Profesor.id == profesor_id).first()
    if not db_profesor:
        raise HTTPException(status_code=404, detail="Profesor no encontrado")
    db.delete(db_profesor)
    db.commit()
    return {"detail": "Profesor eliminado correctamente"}
