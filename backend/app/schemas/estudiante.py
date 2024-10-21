from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

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

    class Config:
        orm_mode = True
