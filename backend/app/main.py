from fastapi import FastAPI
from app.routers import (
    auth,
    estudiantes,
    calificaciones,
    asignaturas,
    profesores,
    administrativos,
    asistencia,
    clases,
    organizaciones,
    ai_module
)
from app.database.connection import connect_db, disconnect_db

app = FastAPI(
    title="Backend Profesional con FastAPI y MariaDB",
    description="API para la gestión de estudiantes, calificaciones, asignaturas, profesores, administrativos y asistencia.",
    version="1.0.0"
)

# Incluir routers
app.include_router(auth.router)
app.include_router(estudiantes.router)
app.include_router(calificaciones.router)
app.include_router(asignaturas.router)
app.include_router(profesores.router)
app.include_router(administrativos.router)
app.include_router(asistencia.router)
app.include_router(clases.router)
app.include_router(organizaciones.router)
app.include_router(ai_module.router)

# Evento de inicio
@app.on_event("startup")
def startup_event():
    connect_db()

# Evento de cierre
@app.on_event("shutdown")
def shutdown_event():
    disconnect_db()
