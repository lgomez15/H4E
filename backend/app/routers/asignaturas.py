from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.asignatura import AsignaturaCreate, AsignaturaRead, AsignaturaUpdate
from app.models.asignatura import Asignatura
from app.database.connection import get_db

router = APIRouter(
    prefix="/asignaturas",
    tags=["Asignaturas"],
)

@router.get("/", response_model=List[AsignaturaRead])
def listar_asignaturas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    asignaturas = db.query(Asignatura).offset(skip).limit(limit).all()
    return asignaturas

@router.get("/{asignatura_id}", response_model=AsignaturaRead)
def obtener_asignatura(asignatura_id: int, db: Session = Depends(get_db)):
    asignatura = db.query(Asignatura).filter(Asignatura.id == asignatura_id).first()
    if not asignatura:
        raise HTTPException(status_code=404, detail="Asignatura no encontrada")
    return asignatura

@router.post("/", response_model=AsignaturaRead)
def crear_asignatura(asignatura: AsignaturaCreate, db: Session = Depends(get_db)):
    db_asignatura = Asignatura(**asignatura.dict())
    db.add(db_asignatura)
    db.commit()
    db.refresh(db_asignatura)
    return db_asignatura

@router.put("/{asignatura_id}", response_model=AsignaturaRead)
def actualizar_asignatura(asignatura_id: int, asignatura: AsignaturaUpdate, db: Session = Depends(get_db)):
    db_asignatura = db.query(Asignatura).filter(Asignatura.id == asignatura_id).first()
    if not db_asignatura:
        raise HTTPException(status_code=404, detail="Asignatura no encontrada")
    for key, value in asignatura.dict(exclude_unset=True).items():
        setattr(db_asignatura, key, value)
    db.commit()
    db.refresh(db_asignatura)
    return db_asignatura

@router.delete("/{asignatura_id}")
def eliminar_asignatura(asignatura_id: int, db: Session = Depends(get_db)):
    db_asignatura = db.query(Asignatura).filter(Asignatura.id == asignatura_id).first()
    if not db_asignatura:
        raise HTTPException(status_code=404, detail="Asignatura no encontrada")
    db.delete(db_asignatura)
    db.commit()
    return {"detail": "Asignatura eliminada correctamente"}
