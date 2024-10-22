# app/database/connection.py

import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
from fastapi import Depends

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("La variable de entorno 'DATABASE_URL' no está definida.")

engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

def get_user_db(db: Session = Depends(get_db)):
    from app.models.user import User  # Importación local para evitar circularidad
    return SQLAlchemyUserDatabase(db, User)
