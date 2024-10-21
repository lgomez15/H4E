# app/schemas/asignatura.py

from __future__ import annotations
from pydantic import BaseModel
from typing import Optional, List

class AsignaturaBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None

class AsignaturaCreate(AsignaturaBase):
    pass

class AsignaturaUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None

class AsignaturaRead(AsignaturaBase):
    id: int
    profesores: List[ProfesorRead] = []
    clases: List[ClaseRead] = []
    estudiantes: List[EstudianteRead] = []
    calificaciones: List[CalificacionRead] = []

    class Config:
        from_attributes = True

# Importar al final para evitar importaciones circulares
from .profesor import ProfesorRead
from .clase import ClaseRead
from .estudiante import EstudianteRead
from .calificacion import CalificacionRead
