from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import relationship
from app.database.connection import Base

class User(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_profesor = Column(Integer, ForeignKey("profesores.id"), nullable=True)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column("password", String(255), nullable=False)  # Cambiado de 'hashed_password' a 'password'
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    profesor = relationship("Profesor", back_populates="user")
