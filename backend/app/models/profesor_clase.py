# app/models/profesor_clase.py

from sqlalchemy import Table, Column, Integer, ForeignKey
from app.database.connection import Base

profesor_clase = Table(
    'profesor_clase',
    Base.metadata,
    Column('profesor_id', Integer, ForeignKey('profesores.id'), primary_key=True),
    Column('clase_id', Integer, ForeignKey('clases.id'), primary_key=True)
)
