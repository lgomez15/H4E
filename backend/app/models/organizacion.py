# app/models/organizacion.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Organizacion(Base):
    __tablename__ = 'organizaciones'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    direccion = Column(String)
    telefono = Column(String)

    clases = relationship('Clase', back_populates='organizacion', cascade='all, delete')
    # Eliminado: administrativos = relationship('Administrativo', back_populates='organizacion')
