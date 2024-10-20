from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.connection import Base
# app/models/administrativo.py


"""
Define el modelo de datos para el personal administrativo, incluyendo sus datos personales y roles dentro de la organización.

Descripción:

    Campos Principales:
        id: Identificador único del personal administrativo.
        nombre y apellido: Nombre y apellido del administrativo.
        email: Correo electrónico único.
        telefono: Número de teléfono opcional.
        puesto: Puesto o rol dentro de la organización.
    Relaciones:
        organizaciones: Relación con las organizaciones donde trabaja el administrativo.

"""


class Administrativo(Base):
    __tablename__ = "administrativos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    telefono = Column(String(20), nullable=True)
    puesto = Column(String(100), nullable=False)

    # Relaciones
    organizaciones = relationship("OrganizacionAdministrativo", back_populates="administrativo")

    def __repr__(self):
        return f"<Administrativo(id={self.id}, nombre={self.nombre}, apellido={self.apellido}, puesto={self.puesto})>"
