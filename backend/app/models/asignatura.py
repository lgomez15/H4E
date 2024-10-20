# app/models/asignatura.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

"""
Define el modelo de datos para las asignaturas que imparten los profesores, incluyendo los exámenes y las calificaciones asociadas.

Descripción:

    Campos Principales:
        id: Identificador único de la asignatura.
        nombre: Nombre de la asignatura.
        descripcion: Descripción opcional de la asignatura.
        profesor_id: Referencia al profesor que imparte la asignatura.
    Relaciones:
        calificaciones: Relación con las calificaciones asociadas a la asignatura.
        profesor: Relación con el profesor que imparte la asignatura.
        clases: Relación con las clases que tienen asignada esta asignatura.
"""

class Asignatura(Base):
    __tablename__ = "asignaturas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255), nullable=True)
    profesor_id = Column(Integer, ForeignKey("profesores.id"), nullable=False)

    # Relaciones
    calificaciones = relationship("Calificacion", back_populates="asignatura")
    profesor = relationship("Profesor", back_populates="asignaturas")
    clases = relationship("ClaseAsignatura", back_populates="asignatura")

    def __repr__(self):
        return f"<Asignatura(id={self.id}, nombre={self.nombre})>"
