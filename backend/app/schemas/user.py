from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional
from app.schemas.profesor import ProfesorRead

class UserRead(BaseModel):
    id: int
    id_profesor: Optional[int] = None
    email: EmailStr
    created_at: Optional[datetime] = None  # Cambiado de str a datetime
    updated_at: Optional[datetime] = None  # Cambiado de str a datetime
    profesor: Optional[ProfesorRead] = None

    class Config:
        from_attributes = True  # Asegúrate de que esto está configurado correctamente


    class Config:
        from_attributes = True  # Actualizado para Pydantic V2

class UserCreate(BaseModel):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True  # Actualizado para Pydantic V2

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None

    class Config:
        from_attributes = True  # Actualizado para Pydantic V2
