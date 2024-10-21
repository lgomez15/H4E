# app/models/estudiante.py

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base
from .estudiante_asignatura import estudiante_asignatura

class Estudiante(Base):
    __tablename__ = 'estudiantes'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)
    fecha_nacimiento = Column(Date)
    email = Column(String, unique=True, index=True)
    clase_id = Column(Integer, ForeignKey('clases.id'))

    clase = relationship('Clase', back_populates='estudiantes')
    datos_contextuales = relationship('DatosContextuales', back_populates='estudiante', uselist=False)
    calificaciones = relationship('Calificacion', back_populates='estudiante')
    asistencias = relationship('Asistencia', back_populates='estudiante')
    asignaturas = relationship('Asignatura', secondary=estudiante_asignatura, back_populates='estudiantes')
