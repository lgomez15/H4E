# app/models/profesor.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
from .profesor_asignatura import profesor_asignatura
from .profesor_clase import profesor_clase


class Profesor(Base):
    __tablename__ = 'profesores'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    telefono = Column(String, nullable=True)
    departamento = Column(String, nullable=True)

    asignaturas = relationship('Asignatura', secondary=profesor_asignatura, back_populates='profesores')
    clases = relationship('Clase', secondary=profesor_clase, back_populates='profesores')
