from pydantic import BaseModel, EmailStr
from typing import Optional

class AdministrativoBase(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    telefono: Optional[str] = None
    puesto: str
    organizacion_id: int

class AdministrativoCreate(AdministrativoBase):
    pass

class AdministrativoUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    email: Optional[EmailStr] = None
    telefono: Optional[str] = None
    puesto: Optional[str] = None
    organizacion_id: Optional[int] = None

class AdministrativoRead(AdministrativoBase):
    id: int

    class Config:
        orm_mode = True
