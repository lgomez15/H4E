# app/models/calificacion.py

from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

"""
Define el modelo de datos para las calificaciones de los estudiantes en diferentes asignaturas y exámenes.

Descripción:

    Campos Principales:
        id: Identificador único de la calificación.
        estudiante_id: Referencia al estudiante que recibe la calificación.
        asignatura_id: Referencia a la asignatura correspondiente.
        examen: Nombre o identificación del examen.
        nota: Nota obtenida en el examen.
    Relaciones:
        estudiante: Relación con el estudiante.
        asignatura: Relación con la asignatura.

"""

class Calificacion(Base):
    __tablename__ = "calificaciones"

    id = Column(Integer, primary_key=True, index=True)
    estudiante_id = Column(Integer, ForeignKey("estudiantes.id"), nullable=False)
    asignatura_id = Column(Integer, ForeignKey("asignaturas.id"), nullable=False)
    examen = Column(String(50), nullable=False)
    nota = Column(Float, nullable=False)

    # Relaciones
    estudiante = relationship("Estudiante", back_populates="calificaciones")
    asignatura = relationship("Asignatura", back_populates="calificaciones")

    def __repr__(self):
        return f"<Calificacion(id={self.id}, estudiante_id={self.estudiante_id}, asignatura_id={self.asignatura_id}, examen={self.examen}, nota={self.nota})>"
