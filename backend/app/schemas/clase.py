# app/schemas/clase.py

from __future__ import annotations
from pydantic import BaseModel
from typing import Optional, List

class ClaseBase(BaseModel):
    nombre: str
    organizacion_id: int

class ClaseCreate(ClaseBase):
    pass

class ClaseUpdate(BaseModel):
    nombre: Optional[str] = None
    organizacion_id: Optional[int] = None

class ClaseRead(ClaseBase):
    id: int
    organizacion: Optional[OrganizacionRead] = None
    estudiantes: List[EstudianteRead] = []
    asignaturas: List[AsignaturaRead] = []
    profesores_ids: List[int] = []  # Agrega esta línea

    class Config:
        from_attributes = True
        fields = {'organizacion': {'exclude': {'clases'}}}

# Importar al final para evitar importaciones circulares
from .organizacion import OrganizacionRead
from .estudiante import EstudianteRead
from .asignatura import AsignaturaRead