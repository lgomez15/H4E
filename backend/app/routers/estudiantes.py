# app/routers/estudiantes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.schemas.estudiante import EstudianteCreate, EstudianteRead, EstudianteUpdate
from app.schemas.calificacion import CalificacionRead
from app.models.estudiante import Estudiante
from app.models.calificacion import Calificacion
from app.database.connection import get_db
from app.schemas.datos_contextuales import DatosContextualesRead
from app.models.datos_contextuales import DatosContextuales
from app.schemas.asistencia import AsistenciaRead
from app.models.asistencia import Asistencia

# Importaciones adicionales para el modelo
import pandas as pd
from joblib import load
import json
import os

# Ruta al directorio donde se encuentran el modelo y las columnas
AI_DIR = os.path.join(os.path.dirname(__file__), 'ai')

# Cargar el modelo entrenado
modelo_path = os.path.join(AI_DIR, 'modelo_entrenado_clasificacion.joblib')
try:
    modelo = load(modelo_path)
    print(f"Modelo cargado desde {modelo_path}")
except FileNotFoundError:
    modelo = None
    print(f"Error: No se encontró el archivo del modelo en {modelo_path}")

# Cargar las columnas utilizadas durante el entrenamiento
columnas_path = os.path.join(AI_DIR, 'columnas.json')
try:
    with open(columnas_path, 'r') as f:
        columnas_modelo = json.load(f)
    print(f"Columnas cargadas desde {columnas_path}")
except FileNotFoundError:
    columnas_modelo = []
    print(f"Error: No se encontró el archivo de columnas en {columnas_path}")

def enviar_email(receiver_email, sender_email, sender_password, texto):
    port = 465  # Puerto para SSL
    smtp_server = 'smtp.gmail.com'

    message = MIMEMultipart("alternative")
    message["Subject"] = "Informe estudiante"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Crear el cuerpo del correo en formato HTML
    html = f"""\
<html>
<body>
    <div class="container">
        <h2>Informe del Estudiante: Ana Ramírez</h2>

        <div class="section">
            <h3>Datos Personales:</h3>
            <p><strong>Nombre:</strong> Ana Ramírez</p>
            <p><strong>Fecha de Nacimiento:</strong> 14 de marzo de 2008 (Edad: 16 años)</p>
            <p><strong>Correo Electrónico:</strong> ana.ramirez@escuela.com</p>
            <p><strong>Dirección:</strong> Urbana</p>
            <p><strong>Sexo:</strong> Femenino</p>
            <p><strong>Clase ID:</strong> 1</p>
        </div>

        <div class="section">
            <h3>Situación Familiar y Escolar:</h3>
            <p><strong>Tamaño de la Familia:</strong> Más de 3 miembros (GT3)</p>
            <p><strong>Relación Familiar:</strong> 4/5</p>
            <p><strong>Padres Viven Juntos:</strong> Sí</p>
            <p><strong>Trabajo de la Madre:</strong> Servicios</p>
            <p><strong>Trabajo del Padre:</strong> Otro</p>
            <p><strong>Nivel Educativo de la Madre:</strong> 3 (Secundaria completa)</p>
            <p><strong>Nivel Educativo del Padre:</strong> 2 (Estudios primarios)</p>
            <p><strong>Tutor:</strong> Madre</p>
            <p><strong>Apoyo Familiar:</strong> Sí</p>
            <p><strong>Asistió a Guardería:</strong> Sí</p>
            <p><strong>Apoyo Escolar Extra:</strong> No</p>
            <p><strong>Acceso a Internet en Casa:</strong> Sí</p>
        </div>

        <div class="section">
            <h3>Actividades y Comportamiento:</h3>
            <p><strong>Actividades Extraescolares:</strong> Participa</p>
            <p><strong>Tiempo Libre:</strong> 4/5</p>
            <p><strong>Salidas Sociales:</strong> 3/5</p>
            <p><strong>Consumo de Alcohol entre Semana:</strong> 1/5</p>
            <p><strong>Consumo de Alcohol durante el Fin de Semana:</strong> 2/5</p>
            <p><strong>Estado de Salud:</strong> 4/5</p>
            <p><strong>Tiempo de Viaje a la Escuela:</strong> Menos de 15 minutos</p>
            <p><strong>Estatus Romántico:</strong> No tiene pareja</p>
            <p><strong>Ausencias Escolares:</strong> 5 días</p>
            <p><strong>Número de Fallos Académicos:</strong> 0</p>
            <p><strong>Tiempo de Estudio Semanal:</strong> 3/5 (entre 5 y 10 horas)</p>
        </div>

        <div class="section">
            <h3>Motivación para Asistir a la Escuela:</h3>
            <p><strong>Razón Principal:</strong> Reputación de la escuela</p>
            <p><strong>Desea Continuar Estudios Superiores:</strong> Sí</p>
        </div>

        <div class="section">
            <h3>Calificaciones Obtenidas:</h3>
            <table class="table-container">
                <thead>
                    <tr>
                        <th>Examen</th>
                        <th>Nota</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Examen Parcial 1</td>
                        <td>88.0</td>
                    </tr>
                    <tr>
                        <td>Examen Parcial 2</td>
                        <td>90.5</td>
                    </tr>
                    <tr>
                        <td>Examen Parcial 3</td>
                        <td>85.0</td>
                    </tr>
                    <tr>
                        <td>Examen Parcial 4</td>
                        <td>87.5</td>
                    </tr>
                    <tr>
                        <td>Examen Final</td>
                        <td>89.0</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="section">
            <h3>Asistencia:</h3>
            <table class="table-container">
                <thead>
                    <tr>
                        <th>Fecha</th>
                        <th>Presente</th>
                        <th>Observaciones</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>01 de abril de 2024</td>
                        <td>Sí</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>02 de abril de 2024</td>
                        <td>Sí</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>03 de abril de 2024</td>
                        <td>No</td>
                        <td>Enfermedad</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="section">
            <h3>Conclusión:</h3>
            <p>Ana Ramírez es una estudiante responsable con buen rendimiento académico y una actitud positiva en cuanto a su tiempo de estudio y participación en actividades extracurriculares. Su salud es buena y tiene un apoyo familiar sólido. A pesar de una ausencia debido a enfermedad, su asistencia general es buena y no ha tenido fracasos académicos. Además, se muestra interesada en continuar con estudios superiores.</p>
        </div>
    </div>
</body>
</html>

    """
    parte_html = MIMEText(html, "html")
    message.attach(parte_html)

    # Conexión segura con el servidor
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email enviado")



router = APIRouter(
    prefix="/estudiantes",
    tags=["Estudiantes"],
)

@router.get("/", response_model=List[EstudianteRead])
def listar_estudiantes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    estudiantes = db.query(Estudiante).offset(skip).limit(limit).all()
    return estudiantes

@router.get("/{estudiante_id}", response_model=EstudianteRead)
def obtener_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    estudiante = db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return estudiante

@router.post("/", response_model=EstudianteRead)
def crear_estudiante(estudiante: EstudianteCreate, db: Session = Depends(get_db)):
    db_estudiante = Estudiante(**estudiante.dict())
    db.add(db_estudiante)
    db.commit()
    db.refresh(db_estudiante)
    return db_estudiante

@router.put("/{estudiante_id}", response_model=EstudianteRead)
def actualizar_estudiante(estudiante_id: int, estudiante: EstudianteUpdate, db: Session = Depends(get_db)):
    db_estudiante = db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()
    if not db_estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    for key, value in estudiante.dict(exclude_unset=True).items():
        setattr(db_estudiante, key, value)
    db.commit()
    db.refresh(db_estudiante)
    return db_estudiante

@router.delete("/{estudiante_id}")
def eliminar_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    db_estudiante = db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()
    if not db_estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    db.delete(db_estudiante)
    db.commit()
    return {"detail": "Estudiante eliminado correctamente"}

@router.get("/datos-contextuales/{estudiante_id}", response_model=DatosContextualesRead)
def obtener_datos_contextuales(estudiante_id: int, db: Session = Depends(get_db)):
    datos = db.query(DatosContextuales).filter(DatosContextuales.estudiante_id == estudiante_id).first()
    if datos is None:
        raise HTTPException(status_code=404, detail="Datos contextuales no encontrados para este estudiante")
    return datos

@router.get("/{estudiante_id}/calificaciones", response_model=List[CalificacionRead])
def obtener_calificaciones_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    estudiante = db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    calificaciones = db.query(Calificacion).filter(Calificacion.estudiante_id == estudiante_id).all()
    return calificaciones


@router.get("/asistencias/{estudiante_id}", response_model=List[AsistenciaRead])
def obtener_asistencias_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    print("estudiante_id", estudiante_id)
    estudiante = db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    asistencias = db.query(Asistencia).filter(Asistencia.estudiante_id == estudiante_id).all()
    return asistencias

#informe a los padres sobre las asistencias, notas y datos contextuales por correo
@router.get("/informe/{estudiante_id}")
def informe_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    estudiante = db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    datos = db.query(DatosContextuales).filter(DatosContextuales.estudiante_id == estudiante_id).first()
    if datos is None:
        raise HTTPException(status_code=404, detail="Datos contextuales no encontrados para este estudiante")
    calificaciones = db.query(Calificacion).filter(Calificacion.estudiante_id == estudiante_id).all()
    asistencias = db.query(Asistencia).filter(Asistencia.estudiante_id == estudiante_id).all()
    texto = {"estudiante": estudiante, "datos": datos, "calificaciones": calificaciones, "asistencias": asistencias}
    enviar_email("gomez@usal.es","iris.contact.service.hack@gmail.com","uvcn rxrg iiaz admx",texto)
    return texto

# Nuevo endpoint para predecir riesgo
@router.get("/prediccion/{estudiante_id}")
def predecir_riesgo(estudiante_id: int, db: Session = Depends(get_db)):
    # Verificar que el modelo y las columnas están cargados
    if modelo is None or not columnas_modelo:
        raise HTTPException(status_code=500, detail="Modelo de predicción no está disponible")

    # Obtener los datos contextuales del estudiante
    datos = db.query(DatosContextuales).filter(DatosContextuales.estudiante_id == estudiante_id).first()
    if datos is None:
        raise HTTPException(status_code=404, detail="Datos contextuales no encontrados para este estudiante")

    # Convertir los datos a un diccionario
    datos_dict = datos.__dict__.copy()

    # Eliminar campos innecesarios
    datos_dict.pop('_sa_instance_state', None)
    datos_dict.pop('id', None)
    datos_dict.pop('estudiante_id', None)

    # Convertir booleanos a 'yes'/'no' si es necesario
    boolean_fields = ['schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic']
    for field in boolean_fields:
        if field in datos_dict:
            datos_dict[field] = 'yes' if datos_dict[field] else 'no'

    # Convertir el diccionario a un DataFrame
    df_nuevo = pd.DataFrame([datos_dict])

    # Preprocesar los datos de la misma forma que durante el entrenamiento
    df_nuevo = pd.get_dummies(df_nuevo)

    # Alinear las columnas con las del modelo
    df_nuevo = df_nuevo.reindex(columns=columnas_modelo, fill_value=0)

    # Hacer la predicción
    try:
        prediccion = modelo.predict(df_nuevo)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al realizar la predicción: {str(e)}")

    # Devolver la predicción
    return {"estudiante_id": estudiante_id, "riesgo": prediccion[0]}