# app/models/__init__.py

from .administrativo import Administrativo
from .asignatura import Asignatura
from .asistencia import Asistencia
from .calificacion import Calificacion
from .clase import Clase
from .datos_contextuales import DatosContextuales
from .estudiante import Estudiante
from .organizacion import Organizacion
from .profesor import Profesor

# Tablas de asociación
from .clase_asignatura import clase_asignatura
from .estudiante_asignatura import estudiante_asignatura
from .profesor_asignatura import profesor_asignatura

#from .ai_module import IARequest, IAResponse

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
    "clase_asignatura",  # Corregido aquí
    "profesor_asignatura",
    "estudiante_asignatura",
    # "IARequest",
    # "IAResponse",
]
