# app/database/__init__.py

from .connection import Base, SessionLocal, engine, get_db

# Si deseas, puedes importar aquí tus modelos para que estén disponibles al importar el paquete `database`.
from app.models import (
    administrativo,
    asignatura,
    asistencia,
    calificacion,
    clase,
    clase_asignatura,
    datos_contextuales,
    estudiante,
    estudiante_asignatura,
    organizacion,
    profesor,
    profesor_asignatura,
)
