# app/schemas/asignatura.py

from __future__ import annotations
from pydantic import BaseModel, ConfigDict
from typing import Optional

class AsignaturaBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    profesor_id: int  # Include this if applicable

class AsignaturaCreate(AsignaturaBase):
    pass

class AsignaturaUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    profesor_id: Optional[int] = None  # Include if you have 'profesor_id'

class AsignaturaRead(AsignaturaBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
