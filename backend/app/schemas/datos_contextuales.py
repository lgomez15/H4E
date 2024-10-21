# app/schemas/datos_contextuales.py

from __future__ import annotations
from pydantic import BaseModel, validator
from typing import Optional, Literal

class DatosContextualesBase(BaseModel):
    estudiante_id: int
    sex: Literal['F', 'M']
    age: int
    address: Literal['U', 'R']
    famsize: Literal['LE3', 'GT3']
    pstatus: Literal['T', 'A']
    medu: int
    fedu: int
    mjob: Literal['teacher', 'health', 'services', 'at_home', 'other']
    fjob: Literal['teacher', 'health', 'services', 'at_home', 'other']
    reason: Literal['home', 'reputation', 'course', 'other']
    guardian: Literal['mother', 'father', 'other']
    traveltime: int
    studytime: int
    failures: int
    schoolsup: bool
    famsup: bool
    paid: bool
    activities: bool
    nursery: bool
    higher: bool
    internet: bool
    romantic: bool
    famrel: int
    freetime: int
    goout: int
    dalc: int
    walc: int
    health: int
    absences: int

    @validator('age')
    def age_must_be_valid(cls, v):
        if not (15 <= v <= 22):
            raise ValueError('La edad debe estar entre 15 y 22 años')
        return v

    @validator('famrel', 'freetime', 'goout', 'dalc', 'walc', 'health')
    def score_must_be_valid(cls, v):
        if not (1 <= v <= 5):
            raise ValueError('El valor debe estar entre 1 y 5')
        return v

class DatosContextualesCreate(DatosContextualesBase):
    pass

class DatosContextualesUpdate(BaseModel):
    sex: Optional[Literal['F', 'M']] = None
    age: Optional[int] = None
    address: Optional[Literal['U', 'R']] = None
    famsize: Optional[Literal['LE3', 'GT3']] = None
    pstatus: Optional[Literal['T', 'A']] = None
    medu: Optional[int] = None
    fedu: Optional[int] = None
    mjob: Optional[Literal['teacher', 'health', 'services', 'at_home', 'other']] = None
    fjob: Optional[Literal['teacher', 'health', 'services', 'at_home', 'other']] = None
    reason: Optional[Literal['home', 'reputation', 'course', 'other']] = None
    guardian: Optional[Literal['mother', 'father', 'other']] = None
    traveltime: Optional[int] = None
    studytime: Optional[int] = None
    failures: Optional[int] = None
    schoolsup: Optional[bool] = None
    famsup: Optional[bool] = None
    paid: Optional[bool] = None
    activities: Optional[bool] = None
    nursery: Optional[bool] = None
    higher: Optional[bool] = None
    internet: Optional[bool] = None
    romantic: Optional[bool] = None
    famrel: Optional[int] = None
    freetime: Optional[int] = None
    goout: Optional[int] = None
    dalc: Optional[int] = None
    walc: Optional[int] = None
    health: Optional[int] = None
    absences: Optional[int] = None

class DatosContextualesRead(DatosContextualesBase):
    id: int
    estudiante: Optional[EstudianteRead] = None

    class Config:
        from_attributes = True

# Importar al final para evitar importaciones circulares
from .estudiante import EstudianteRead
