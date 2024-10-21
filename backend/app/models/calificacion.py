from sqlalchemy import Column, Integer, ForeignKey, Float, String
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Calificacion(Base):
    __tablename__ = 'calificaciones'

    id = Column(Integer, primary_key=True, index=True)
    estudiante_id = Column(Integer, ForeignKey('estudiantes.id'))
    asignatura_id = Column(Integer, ForeignKey('asignaturas.id'))
    examen = Column(String)
    nota = Column(Float)

    estudiante = relationship('Estudiante', back_populates='calificaciones')
    asignatura = relationship('Asignatura', back_populates='calificaciones')
