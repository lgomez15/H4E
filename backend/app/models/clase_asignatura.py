# app/models/clase_asignatura.py

from sqlalchemy import Table, Column, Integer, ForeignKey
from app.database.connection import Base

clase_asignatura = Table(
    'clase_asignatura',
    Base.metadata,
    Column('clase_id', Integer, ForeignKey('clases.id'), primary_key=True),
    Column('asignatura_id', Integer, ForeignKey('asignaturas.id'), primary_key=True)
)
