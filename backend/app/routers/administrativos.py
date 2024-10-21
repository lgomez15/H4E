from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.administrativo import AdministrativoCreate, AdministrativoRead, AdministrativoUpdate
from app.models.administrativo import Administrativo
from app.database.connection import get_db

router = APIRouter(
    prefix="/administrativos",
    tags=["Administrativos"],
)

@router.get("/", response_model=List[AdministrativoRead])
def listar_administrativos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    administrativos = db.query(Administrativo).offset(skip).limit(limit).all()
    return administrativos

@router.get("/{administrativo_id}", response_model=AdministrativoRead)
def obtener_administrativo(administrativo_id: int, db: Session = Depends(get_db)):
    administrativo = db.query(Administrativo).filter(Administrativo.id == administrativo_id).first()
    if not administrativo:
        raise HTTPException(status_code=404, detail="Administrativo no encontrado")
    return administrativo

@router.post("/", response_model=AdministrativoRead)
def crear_administrativo(administrativo: AdministrativoCreate, db: Session = Depends(get_db)):
    db_administrativo = Administrativo(**administrativo.dict())
    db.add(db_administrativo)
    db.commit()
    db.refresh(db_administrativo)
    return db_administrativo

@router.put("/{administrativo_id}", response_model=AdministrativoRead)
def actualizar_administrativo(administrativo_id: int, administrativo: AdministrativoUpdate, db: Session = Depends(get_db)):
    db_administrativo = db.query(Administrativo).filter(Administrativo.id == administrativo_id).first()
    if not db_administrativo:
        raise HTTPException(status_code=404, detail="Administrativo no encontrado")
    for key, value in administrativo.dict(exclude_unset=True).items():
        setattr(db_administrativo, key, value)
    db.commit()
    db.refresh(db_administrativo)
    return db_administrativo

@router.delete("/{administrativo_id}")
def eliminar_administrativo(administrativo_id: int, db: Session = Depends(get_db)):
    db_administrativo = db.query(Administrativo).filter(Administrativo.id == administrativo_id).first()
    if not db_administrativo:
        raise HTTPException(status_code=404, detail="Administrativo no encontrado")
    db.delete(db_administrativo)
    db.commit()
    return {"detail": "Administrativo eliminado correctamente"}
