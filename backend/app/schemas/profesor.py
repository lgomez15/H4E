# app/schemas/profesor.py

from __future__ import annotations
from pydantic import BaseModel, EmailStr
from typing import Optional, List

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

    class Config:
        from_attributes = True

# Importar al final para evitar importaciones circulares
from .asignatura import AsignaturaRead
