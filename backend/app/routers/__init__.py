from .estudiantes import router as estudiantes_router
from .profesores import router as profesores_router
from .asignaturas import router as asignaturas_router
from .clases import router as clases_router
from .administrativos import router as administrativos_router
from .asistencia import router as asistencia_router
from .calificaciones import router as calificaciones_router
from .organizaciones import router as organizaciones_router
from .datos_contextuales import router as datos_contextuales_router
# from .ai_module import router as ai_module_router  # Descomenta si tienes este módulo

__all__ = [
    "estudiantes_router",
    "profesores_router",
    "asignaturas_router",
    "clases_router",
    "administrativos_router",
    "asistencia_router",  # Changed from 'asistencias_router' to 'asistencia_router'
    "calificaciones_router",
    "organizaciones_router",
    "datos_contextuales_router",
    # "ai_module_router",
]
