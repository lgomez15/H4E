from __future__ import annotations
from pydantic import BaseModel, EmailStr
from typing import Optional, List

# Asegúrate de que AsignaturaRead está definido en app/schemas/asignatura.py
class AsignaturaRead(BaseModel):
    id: int
    nombre: str

    class Config:
        from_attributes = True

class ProfesorBase(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    telefono: Optional[str] = None
    departamento: Optional[str] = None

class ProfesorCreate(ProfesorBase):
    pass

class ProfesorUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    email: Optional[EmailStr] = None
    telefono: Optional[str] = None
    departamento: Optional[str] = None

class ProfesorRead(ProfesorBase):
    id: int
    asignaturas: List[AsignaturaRead] = []
    clases_ids: List[int] = []

    class Config:
        from_attributes = True
