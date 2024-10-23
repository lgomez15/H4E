# app/models/estudiante_asignatura.py

from sqlalchemy import Table, Column, Integer, ForeignKey
from app.database.connection import Base

estudiante_asignatura = Table(
    'estudiante_asignatura',
    Base.metadata,
    Column('estudiante_id', Integer, ForeignKey('estudiantes.id'), primary_key=True),
    Column('asignatura_id', Integer, ForeignKey('asignaturas.id'), primary_key=True)
)
