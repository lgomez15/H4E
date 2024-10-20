# app/models/__init__.py

"""
Este archivo convierte la carpeta models en un paquete de Python, permitiendo importar fácilmente los modelos desde otras partes de la aplicación.
"""

from .estudiante import Estudiante
from .calificacion import Calificacion
from .asignatura import Asignatura
from .profesor import Profesor
from .administrativo import Administrativo
from .asistencia import Asistencia

__all__ = [
    "Estudiante",
    "Calificacion",
    "Asignatura",
    "Profesor",
    "Administrativo",
    "Asistencia",
]
