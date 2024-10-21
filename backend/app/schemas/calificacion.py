from pydantic import BaseModel
from typing import Optional

class CalificacionBase(BaseModel):
    estudiante_id: int
    asignatura_id: int
    examen: str
    nota: float

class CalificacionCreate(CalificacionBase):
    pass

class CalificacionUpdate(BaseModel):
    estudiante_id: Optional[int] = None
    asignatura_id: Optional[int] = None
    examen: Optional[str] = None
    nota: Optional[float] = None

class CalificacionRead(CalificacionBase):
    id: int

    class Config:
        orm_mode = True
