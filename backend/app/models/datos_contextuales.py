# app/models/datos_contextuales.py

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

class DatosContextuales(Base):
    __tablename__ = 'datos_contextuales'

    id = Column(Integer, primary_key=True, index=True)
    estudiante_id = Column(Integer, ForeignKey('estudiantes.id'), unique=True)
    sex = Column(String)
    age = Column(Integer)
    address = Column(String)
    famsize = Column(String)
    pstatus = Column(String)
    medu = Column(Integer)
    fedu = Column(Integer)
    mjob = Column(String)
    fjob = Column(String)
    reason = Column(String)
    guardian = Column(String)
    traveltime = Column(Integer)
    studytime = Column(Integer)
    failures = Column(Integer)
    schoolsup = Column(Boolean, default=False)
    famsup = Column(Boolean, default=False)
    paid = Column(Boolean, default=False)
    activities = Column(Boolean, default=False)
    nursery = Column(Boolean, default=False)
    higher = Column(Boolean, default=False)
    internet = Column(Boolean, default=False)
    romantic = Column(Boolean, default=False)
    famrel = Column(Integer)
    freetime = Column(Integer)
    goout = Column(Integer)
    dalc = Column(Integer)
    walc = Column(Integer)
    health = Column(Integer)
    absences = Column(Integer)

    estudiante = relationship('Estudiante', back_populates='datos_contextuales')
