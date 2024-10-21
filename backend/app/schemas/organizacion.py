# app/schemas/organizacion.py

from __future__ import annotations
from pydantic import BaseModel
from typing import Optional, List

class OrganizacionBase(BaseModel):
    nombre: str
    direccion: str

class OrganizacionCreate(OrganizacionBase):
    pass

class OrganizacionUpdate(BaseModel):
    nombre: Optional[str] = None
    direccion: Optional[str] = None

class OrganizacionRead(OrganizacionBase):
    id: int
    clases: List[ClaseRead] = []
    administrativos: List[AdministrativoRead] = []

    class Config:
        from_attributes = True

# Importar al final para evitar importaciones circulares
from .clase import ClaseRead
from .administrativo import AdministrativoRead
