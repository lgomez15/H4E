# app/database/connection.py

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la URL de la base de datos desde las variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("La variable de entorno 'DATABASE_URL' no está definida.")

# Crear el motor de la base de datos
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Habilitar el log de SQL para depuración
    pool_pre_ping=True  # Verificar conexiones antes de usarlas
)

# Crear una fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base para los modelos
Base = declarative_base()

def get_db():
    """
    Generador que proporciona una sesión de base de datos y se asegura de cerrarla después de usarla.
    Utilizado como dependencia en las rutas de FastAPI.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
