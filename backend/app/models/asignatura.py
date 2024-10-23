# app/models/asignatura.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from .profesor_asignatura import profesor_asignatura
from .clase_asignatura import clase_asignatura
from .estudiante_asignatura import estudiante_asignatura

class Asignatura(Base):
    __tablename__ = 'asignaturas'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(Text, nullable=True)

    profesores = relationship('Profesor', secondary=profesor_asignatura, back_populates='asignaturas')
    clases = relationship('Clase', secondary=clase_asignatura, back_populates='asignaturas')
    estudiantes = relationship('Estudiante', secondary=estudiante_asignatura, back_populates='asignaturas')

    calificaciones = relationship('Calificacion', back_populates='asignatura')
