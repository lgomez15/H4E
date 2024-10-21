# app/main.py

import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.connection import engine, Base
from app.routers import (
    estudiantes_router,
    profesores_router,
    asignaturas_router,
    clases_router,
    administrativos_router,
    asistencia_router,  # Changed from 'asistencias_router' to 'asistencia_router'
    calificaciones_router,
    organizaciones_router,
    datos_contextuales_router,
    # ai_module_router,  # Descomenta esta línea si tienes este módulo
)

# Configuración de logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)
logger.info("Todas las tablas han sido creadas en la base de datos.")

# Instancia de la aplicación FastAPI
app = FastAPI(
    title="API de Gestión Educativa",
    description="API para gestionar estudiantes, profesores, asignaturas y más.",
    version="1.0.0"
)

# Configuración de CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir todos los orígenes: ["*"]
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)
logger.info("Middleware de CORS configurado.")

# Include routers
app.include_router(estudiantes_router)
app.include_router(profesores_router)
app.include_router(asignaturas_router)
app.include_router(clases_router)
app.include_router(administrativos_router)
app.include_router(asistencia_router)  # Corrected router name
app.include_router(calificaciones_router)
app.include_router(organizaciones_router)
app.include_router(datos_contextuales_router)
# app.include_router(ai_module_router)  # Descomenta esta línea si tienes este módulo
logger.info("Routers incluidos en la aplicación.")

# Endpoint raíz
@app.get("/", tags=["Root"])
def read_root():
    logger.info("Endpoint raíz accedido.")
    return {"message": "Bienvenido a la API de Gestión Educativa"}

# Manejo de excepciones globales (opcional)
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.requests import Request

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(f"Error de validación: {exc}")
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body},
    )

# Evento al iniciar la aplicación
@app.on_event("startup")
async def startup_event():
    logger.info("La aplicación ha iniciado.")

# Evento al cerrar la aplicación
@app.on_event("shutdown")
async def shutdown_event():
    logger.info("La aplicación se ha detenido.")
