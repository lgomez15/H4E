from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Administrativo(Base):
    __tablename__ = 'administrativos'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    telefono = Column(String, nullable=True)
    puesto = Column(String)
    organizacion_id = Column(Integer, ForeignKey('organizaciones.id'))

    organizacion = relationship('Organizacion', back_populates='administrativos')
