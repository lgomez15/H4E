# app/models/organizacion.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Organizacion(Base):
    __tablename__ = 'organizaciones'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    direccion = Column(String)

    clases = relationship('Clase', back_populates='organizacion')
    administrativos = relationship('Administrativo', back_populates='organizacion')
