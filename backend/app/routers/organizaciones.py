from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.organizacion import OrganizacionCreate, OrganizacionRead, OrganizacionUpdate
from app.models.organizacion import Organizacion
from app.database.connection import get_db

router = APIRouter(
    prefix="/organizaciones",
    tags=["Organizaciones"],
)

@router.get("/", response_model=List[OrganizacionRead])
def listar_organizaciones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    organizaciones = db.query(Organizacion).offset(skip).limit(limit).all()
    return organizaciones

@router.get("/{organizacion_id}", response_model=OrganizacionRead)
def obtener_organizacion(organizacion_id: int, db: Session = Depends(get_db)):
    organizacion = db.query(Organizacion).filter(Organizacion.id == organizacion_id).first()
    if not organizacion:
        raise HTTPException(status_code=404, detail="Organización no encontrada")
    return organizacion

@router.post("/", response_model=OrganizacionRead)
def crear_organizacion(organizacion: OrganizacionCreate, db: Session = Depends(get_db)):
    db_organizacion = Organizacion(**organizacion.dict())
    db.add(db_organizacion)
    db.commit()
    db.refresh(db_organizacion)
    return db_organizacion

@router.put("/{organizacion_id}", response_model=OrganizacionRead)
def actualizar_organizacion(organizacion_id: int, organizacion: OrganizacionUpdate, db: Session = Depends(get_db)):
    db_organizacion = db.query(Organizacion).filter(Organizacion.id == organizacion_id).first()
    if not db_organizacion:
        raise HTTPException(status_code=404, detail="Organización no encontrada")
    for key, value in organizacion.dict(exclude_unset=True).items():
        setattr(db_organizacion, key, value)
    db.commit()
    db.refresh(db_organizacion)
    return db_organizacion

@router.delete("/{organizacion_id}")
def eliminar_organizacion(organizacion_id: int, db: Session = Depends(get_db)):
    db_organizacion = db.query(Organizacion).filter(Organizacion.id == organizacion_id).first()
    if not db_organizacion:
        raise HTTPException(status_code=404, detail="Organización no encontrada")
    db.delete(db_organizacion)
    db.commit()
    return {"detail": "Organización eliminada correctamente"}
