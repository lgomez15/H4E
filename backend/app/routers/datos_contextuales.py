from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.datos_contextuales import DatosContextualesCreate, DatosContextualesRead, DatosContextualesUpdate
from app.models.datos_contextuales import DatosContextuales
from app.database.connection import get_db

router = APIRouter(
    prefix="/datos_contextuales",
    tags=["Datos Contextuales"],
)

@router.get("/", response_model=List[DatosContextualesRead])
def listar_datos_contextuales(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    datos = db.query(DatosContextuales).offset(skip).limit(limit).all()
    return datos

@router.get("/{datos_id}", response_model=DatosContextualesRead)
def obtener_datos_contextuales(datos_id: int, db: Session = Depends(get_db)):
    datos = db.query(DatosContextuales).filter(DatosContextuales.id == datos_id).first()
    if not datos:
        raise HTTPException(status_code=404, detail="Datos contextuales no encontrados")
    return datos

@router.post("/", response_model=DatosContextualesRead)
def crear_datos_contextuales(datos: DatosContextualesCreate, db: Session = Depends(get_db)):
    db_datos = DatosContextuales(**datos.dict())
    db.add(db_datos)
    db.commit()
    db.refresh(db_datos)
    return db_datos

@router.put("/{datos_id}", response_model=DatosContextualesRead)
def actualizar_datos_contextuales(datos_id: int, datos: DatosContextualesUpdate, db: Session = Depends(get_db)):
    db_datos = db.query(DatosContextuales).filter(DatosContextuales.id == datos_id).first()
    if not db_datos:
        raise HTTPException(status_code=404, detail="Datos contextuales no encontrados")
    for key, value in datos.dict(exclude_unset=True).items():
        setattr(db_datos, key, value)
    db.commit()
    db.refresh(db_datos)
    return db_datos

@router.delete("/{datos_id}")
def eliminar_datos_contextuales(datos_id: int, db: Session = Depends(get_db)):
    db_datos = db.query(DatosContextuales).filter(DatosContextuales.id == datos_id).first()
    if not db_datos:
        raise HTTPException(status_code=404, detail="Datos contextuales no encontrados")
    db.delete(db_datos)
    db.commit()
    return {"detail": "Datos contextuales eliminados correctamente"}
