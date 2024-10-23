from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.clase import ClaseCreate, ClaseRead, ClaseUpdate
from app.models.clase import Clase
from app.database.connection import get_db

router = APIRouter(
    prefix="/clases",
    tags=["Clases"],
)

@router.get("/", response_model=List[ClaseRead])
def listar_clases(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clases = db.query(Clase).offset(skip).limit(limit).all()
    return clases

@router.get("/{clase_id}", response_model=ClaseRead)
def obtener_clase(clase_id: int, db: Session = Depends(get_db)):
    clase = db.query(Clase).filter(Clase.id == clase_id).first()
    if not clase:
        raise HTTPException(status_code=404, detail="Clase no encontrada")
    return clase

@router.post("/", response_model=ClaseRead)
def crear_clase(clase: ClaseCreate, db: Session = Depends(get_db)):
    db_clase = Clase(**clase.dict())
    db.add(db_clase)
    db.commit()
    db.refresh(db_clase)
    return db_clase

@router.put("/{clase_id}", response_model=ClaseRead)
def actualizar_clase(clase_id: int, clase: ClaseUpdate, db: Session = Depends(get_db)):
    db_clase = db.query(Clase).filter(Clase.id == clase_id).first()
    if not db_clase:
        raise HTTPException(status_code=404, detail="Clase no encontrada")
    for key, value in clase.dict(exclude_unset=True).items():
        setattr(db_clase, key, value)
    db.commit()
    db.refresh(db_clase)
    return db_clase

@router.delete("/{clase_id}")
def eliminar_clase(clase_id: int, db: Session = Depends(get_db)):
    db_clase = db.query(Clase).filter(Clase.id == clase_id).first()
    if not db_clase:
        raise HTTPException(status_code=404, detail="Clase no encontrada")
    db.delete(db_clase)
    db.commit()
    return {"detail": "Clase eliminada correctamente"}
