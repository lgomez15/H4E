# app/schemas/organizacion.py

from pydantic import BaseModel
from typing import Optional, List
from .clase import ClaseRead

class OrganizacionBase(BaseModel):
    nombre: str
    direccion: str
    telefono: str

class OrganizacionCreate(OrganizacionBase):
    pass

class OrganizacionUpdate(BaseModel):
    nombre: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None

class OrganizacionRead(OrganizacionBase):
    id: int
    #clases: List[ClaseRead] = []
    # Eliminado: administrativos: List[AdministrativoRead] = []

    class Config:
        from_attributes = True
