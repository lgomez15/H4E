from pydantic import BaseModel
from datetime import date
from typing import Optional

class AsistenciaBase(BaseModel):
    estudiante_id: int
    fecha: date
    presente: bool
    observaciones: Optional[str] = None

class AsistenciaCreate(AsistenciaBase):
    pass

class AsistenciaUpdate(BaseModel):
    estudiante_id: Optional[int] = None
    fecha: Optional[date] = None
    presente: Optional[bool] = None
    observaciones: Optional[str] = None

class AsistenciaRead(AsistenciaBase):
    id: int

    class Config:
        orm_mode = True  # Si usas Pydantic v1
        # from_attributes = True  # Si usas Pydantic v2
