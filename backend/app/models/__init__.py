# app/models/__init__.py

#from .administrativo import Administrativo
from .asignatura import Asignatura
from .asistencia import Asistencia
from .calificacion import Calificacion
from .clase import Clase
from .datos_contextuales import DatosContextuales
from .estudiante import Estudiante
from .organizacion import Organizacion
from .profesor import Profesor
from .user import User

# Tablas de asociación
from .clase_asignatura import clase_asignatura
from .estudiante_asignatura import estudiante_asignatura
from .profesor_asignatura import profesor_asignatura
from .profesor_clase import profesor_clase

__all__ = [
    "Estudiante",
    "Calificacion",
    "Asignatura",
    "Profesor",
    "Administrativo",
    "Asistencia",
    "Clase",
    "Organizacion",
    "DatosContextuales",
    "clase_asignatura",
    "profesor_asignatura",
    "estudiante_asignatura",
    "profesor_clase",
    "User",
]
