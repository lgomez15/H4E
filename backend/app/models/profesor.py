# app/models/profesor.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.connection import Base

"""
Define el modelo de datos para los profesores, incluyendo sus datos personales y las asignaturas que imparten.

Descripción:

    Campos Principales:
        id: Identificador único del profesor.
        nombre y apellido: Nombre y apellido del profesor.
        email: Correo electrónico único del profesor.
        telefono: Número de teléfono opcional.
        departamento: Departamento al que pertenece el profesor.
    Relaciones:
        asignaturas: Relación con las asignaturas que imparte.
        organizaciones: Relación con las organizaciones donde trabaja el profesor.

"""
class Profesor(Base):
    __tablename__ = "profesores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    telefono = Column(String(20), nullable=True)
    departamento = Column(String(100), nullable=True)

    # Relaciones
    asignaturas = relationship("Asignatura", back_populates="profesor")
    organizaciones = relationship("OrganizacionProfesor", back_populates="profesor")

    def __repr__(self):
        return f"<Profesor(id={self.id}, nombre={self.nombre}, apellido={self.apellido})>"
