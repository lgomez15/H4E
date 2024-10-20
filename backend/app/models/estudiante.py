# app/models/estudiante.py

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

"""
Define el modelo de datos para los estudiantes, incluyendo sus atributos y relaciones con otras tablas si las hubiera.


Descripción:

    Campos Principales:
        id: Identificador único del estudiante.
        nombre y apellido: Nombre y apellido del estudiante.
        fecha_nacimiento: Fecha de nacimiento del estudiante.
        email: Correo electrónico único del estudiante.
        clase_id: Referencia a la clase a la que pertenece el estudiante.
    Relaciones:
        calificaciones: Relación con las calificaciones del estudiante.
        asistencias: Relación con los registros de asistencia del estudiante.
        clase: Relación con la clase a la que pertenece.
"""
class Estudiante(Base):
    __tablename__ = "estudiantes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    clase_id = Column(Integer, ForeignKey("clases.id"), nullable=False)

    # Relaciones
    calificaciones = relationship("Calificacion", back_populates="estudiante")
    clase = relationship("Clase", back_populates="estudiantes")

    def __repr__(self):
        return f"<Estudiante(id={self.id}, nombre={self.nombre}, apellido={self.apellido})>"

