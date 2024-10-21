# app/schemas/calificacion.py

from __future__ import annotations
from pydantic import BaseModel, ConfigDict
from typing import Optional

class CalificacionBase(BaseModel):
    asignatura_id: int
    estudiante_id: int
    nota: float

class CalificacionCreate(CalificacionBase):
    pass

class CalificacionUpdate(BaseModel):
    asignatura_id: Optional[int] = None
    estudiante_id: Optional[int] = None
    nota: Optional[float] = None

class CalificacionRead(CalificacionBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
