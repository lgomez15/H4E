# app/schemas/estudiante.py

from __future__ import annotations
from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import date

from .datos_contextuales import DatosContextualesRead  # Import directly since there's no circular dependency

class EstudianteBase(BaseModel):
    nombre: str
    apellido: str
    fecha_nacimiento: date
    email: EmailStr
    clase_id: int

class EstudianteCreate(EstudianteBase):
    pass

class EstudianteUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    email: Optional[EmailStr] = None
    clase_id: Optional[int] = None

class EstudianteRead(EstudianteBase):
    id: int
    datos_contextuales: Optional[DatosContextualesRead] = None

    model_config = ConfigDict(from_attributes=True)
