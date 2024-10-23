# app/schemas/administrativo.py

from pydantic import BaseModel, EmailStr
from typing import Optional

class AdministrativoBase(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    telefono: Optional[str] = None
    puesto: str

class AdministrativoCreate(AdministrativoBase):
    pass

class AdministrativoUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    email: Optional[EmailStr] = None
    telefono: Optional[str] = None
    puesto: Optional[str] = None

class AdministrativoRead(AdministrativoBase):
    id: int

    class Config:
        from_attributes = True
