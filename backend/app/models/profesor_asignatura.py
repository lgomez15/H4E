# app/models/profesor_asignatura.py

from sqlalchemy import Table, Column, Integer, ForeignKey
from app.database.connection import Base

profesor_asignatura = Table(
    'profesor_asignatura',
    Base.metadata,
    Column('profesor_id', Integer, ForeignKey('profesores.id'), primary_key=True),
    Column('asignatura_id', Integer, ForeignKey('asignaturas.id'), primary_key=True)
)
