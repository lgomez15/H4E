import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def connect_db():
    # TODO: Implementar lógica para conectar a la base de datos
    pass

def disconnect_db():
    # TODO: Implementar lógica para desconectar de la base de datos
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
