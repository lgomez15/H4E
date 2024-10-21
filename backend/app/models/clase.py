# app/models/clase.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from .clase_asignatura import clase_asignatura
from .profesor_clase import profesor_clase

class Clase(Base):
    __tablename__ = 'clases'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    organizacion_id = Column(Integer, ForeignKey('organizaciones.id'))

    organizacion = relationship('Organizacion', back_populates='clases')
    estudiantes = relationship('Estudiante', back_populates='clase')
    asignaturas = relationship('Asignatura', secondary=clase_asignatura, back_populates='clases')
    profesores = relationship('Profesor', secondary=profesor_clase, back_populates='clases')
