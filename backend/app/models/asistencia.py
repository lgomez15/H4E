from sqlalchemy import Column, Integer, ForeignKey, Date, Boolean, String
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Asistencia(Base):
    __tablename__ = 'asistencias'

    id = Column(Integer, primary_key=True, index=True)
    estudiante_id = Column(Integer, ForeignKey('estudiantes.id'))
    fecha = Column(Date)
    presente = Column(Boolean)
    observaciones = Column(String, nullable=True)

    estudiante = relationship('Estudiante', back_populates='asistencias')
