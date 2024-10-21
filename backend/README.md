¡Excelente! Me alegra saber que tu proyecto está funcionando mejor. A continuación, te proporcionaré un archivo `.gitignore` adecuado para tu proyecto y un `README.md` con la descripción general, así como las llamadas necesarias para probar tus endpoints en Postman.

---

## **1. Archivo `.gitignore`**

### **Ubicación:**
Coloca el archivo `.gitignore` en la **raíz** de tu proyecto (`C:\Users\luisg\Desktop\Archive\backend\`).

### **Contenido del `.gitignore`:**

```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# Virtual environment
venv/
ENV/
env/
env.bak/
venv.bak/

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# IDEs and Editors
# PyCharm
.idea/
*.iml
*.ipr
*.iws

# VS Code
.vscode/

# Sublime Text
*.sublime-project
*.sublime-workspace

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# macOS
.DS_Store

# Windows
Thumbs.db
ehthumbs.db
Desktop.ini

# Logs
*.log

# SQLAlchemy SQLite database (if used)
*.db

# Alembic migrations
alembic.ini
alembic/
```

---

## **2. Archivo `README.md`**

### **Ubicación:**
Coloca el archivo `README.md` en la **raíz** de tu proyecto (`C:\Users\luisg\Desktop\Archive\backend\`).

### **Contenido del `README.md`:**

```markdown
# Escuela Backend API

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## **Descripción**

**Escuela Backend API** es una API desarrollada con **FastAPI** que gestiona las operaciones de una institución educativa. Permite gestionar organizaciones, clases, profesores, asignaturas, administrativos, estudiantes, calificaciones, asistencias y datos contextuales de los estudiantes. La API está construida utilizando **SQLAlchemy** como ORM y **MariaDB** como sistema de gestión de bases de datos.

## **Características**

- **Gestión de Organizaciones:** Crear, leer, actualizar y eliminar organizaciones educativas.
- **Gestión de Clases:** Administrar clases asociadas a organizaciones.
- **Gestión de Profesores:** Manejar información de profesores y sus asignaturas.
- **Gestión de Asignaturas:** Administrar las asignaturas ofrecidas y sus detalles.
- **Gestión de Administrativos:** Gestionar personal administrativo de la institución.
- **Gestión de Estudiantes:** Crear y gestionar información de estudiantes.
- **Calificaciones y Asistencias:** Registrar y consultar calificaciones y asistencias de los estudiantes.
- **Datos Contextuales:** Almacenar información contextual adicional sobre los estudiantes.

## **Tecnologías Utilizadas**

- **Python 3.12**
- **FastAPI**
- **SQLAlchemy**
- **MariaDB**
- **Alembic** (para migraciones de base de datos)
- **Pydantic**
- **Uvicorn** (servidor ASGI)
- **Git** (control de versiones)

## **Pre-requisitos**

- **Python 3.12** instalado en tu sistema.
- **MariaDB** instalado y ejecutándose.
- **Git** instalado para el control de versiones.

## **Instalación**

1. **Clonar el Repositorio**

   ```bash
   git clone https://github.com/tu-usuario/escuela-backend.git
   cd escuela-backend
   ```

2. **Crear y Activar un Entorno Virtual**

   ```bash
   python -m venv venv
   # En Windows
   venv\Scripts\activate
   # En macOS/Linux
   source venv/bin/activate
   ```

3. **Instalar las Dependencias**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## **Configuración**

1. **Configurar Variables de Entorno**

   Crea un archivo `.env` en la raíz del proyecto y agrega la siguiente configuración, reemplazando los valores según tu entorno:

   ```env
   DATABASE_URL=mariadb+mariadbconnector://usuario:contraseña@localhost:3306/escuela
   ```

2. **Configurar la Base de Datos**

   Asegúrate de que MariaDB esté ejecutándose y que la base de datos `escuela` exista. Puedes crearla con:

   ```sql
   CREATE DATABASE escuela;
   ```

3. **Aplicar Migraciones con Alembic**

   Inicializa y aplica las migraciones para crear las tablas necesarias en la base de datos.

   ```bash
   alembic upgrade head
   ```

   Si aún no has configurado Alembic, sigue estos pasos:

   ```bash
   alembic init alembic
   # Edita alembic.ini y alembic/env.py según las instrucciones proporcionadas anteriormente
   alembic revision --autogenerate -m "Initial migration"
   alembic upgrade head
   ```

## **Ejecutar la Aplicación**

Inicia el servidor de desarrollo con Uvicorn:

```bash
uvicorn app.main:app --reload --log-level debug
```

La API estará disponible en `http://127.0.0.1:8000`.

## **Documentación de la API**

FastAPI genera automáticamente documentación interactiva que puedes acceder en:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## **Uso de la API**

### **Obtener Todos los Estudiantes de una Clase**

- **Endpoint:** `GET /estudiantes/clase/{clase_id}`
- **Descripción:** Obtiene una lista de todos los estudiantes que pertenecen a la clase especificada por `clase_id`.
- **Parámetros:**
  - `clase_id` (int): ID de la clase.
- **Respuesta Exitosa:**
  - **Código:** `200 OK`
  - **Contenido:**
    ```json
    [
        {
            "id": 1,
            "nombre": "Luis",
            "apellido": "Hernández",
            "fecha_nacimiento": "2008-05-15",
            "email": "luis.hernandez@escuela.com",
            "clase_id": 1
        },
        {
            "id": 2,
            "nombre": "Sofía",
            "apellido": "Torres",
            "fecha_nacimiento": "2009-08-22",
            "email": "sofia.torres@escuela.com",
            "clase_id": 2
        }
    ]
    ```

## **Estructura del Proyecto**

```
backend/
├── app/
│   ├── main.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── estudiantes.py
│   │   ├── profesores.py
│   │   ├── asignaturas.py
│   │   ├── clases.py
│   │   ├── administrativos.py
│   │   ├── asistencias.py
│   │   ├── calificaciones.py
│   │   ├── organizaciones.py
│   │   └── datos_contextuales.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── administrativo.py
│   │   ├── asignatura.py
│   │   ├── asistencia.py
│   │   ├── calificacion.py
│   │   ├── clase.py
│   │   ├── datos_contextuales.py
│   │   ├── estudiante.py
│   │   ├── organizacion.py
│   │   ├── profesor.py
│   │   ├── clase_asignatura.py
│   │   ├── estudiante_asignatura.py
│   │   └── profesor_asignatura.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── administrativo.py
│   │   ├── asignatura.py
│   │   ├── asistencia.py
│   │   ├── calificacion.py
│   │   ├── clase.py
│   │   ├── datos_contextuales.py
│   │   ├── estudiante.py
│   │   ├── organizacion.py
│   │   └── profesor.py
│   └── database/
│       ├── __init__.py
│       └── connection.py
├── alembic/
├── venv/
├── .gitignore
├── README.md
└── requirements.txt
```

## **Contribución**

¡Contribuciones son bienvenidas! Por favor, sigue estos pasos para contribuir:

1. **Fork** el repositorio.
2. Crea una **rama** para tu feature (`git checkout -b feature/nueva-funcionalidad`).
3. **Commitea** tus cambios (`git commit -m 'Añadir nueva funcionalidad'`).
4. **Push** a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un **Pull Request**.

## **Licencia**

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## **Contacto**

Para cualquier consulta o sugerencia, por favor, contacta a:

- **Nombre:** Luis García
- **Email:** luis.garcia@ejemplo.com

---

## **3. Llamadas para Postman para Testear los Endpoints**

A continuación, te proporciono las llamadas necesarias para probar todos los endpoints definidos en tu API. Puedes importar estas solicitudes directamente en Postman o configurarlas manualmente siguiendo las instrucciones.

### **Configuración Inicial en Postman**

1. **Crear un Nuevo Entorno:**
   - **Nombre:** Escuela Backend
   - **Variable:** `base_url` = `http://127.0.0.1:8000`

2. **Headers Comunes:**
   - Para todas las solicitudes que envían datos (POST, PUT), asegúrate de agregar:
     - **Key:** `Content-Type`
     - **Value:** `application/json`

### **Endpoints por Recurso**

#### **1. Organizaciones**

##### **a. Obtener Todas las Organizaciones**

- **Método:** GET
- **URL:** `{{base_url}}/organizaciones`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

##### **b. Obtener una Organización por ID**

- **Método:** GET
- **URL:** `{{base_url}}/organizaciones/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

**Ejemplo:**

```http
GET http://127.0.0.1:8000/organizaciones/1
```

##### **c. Crear una Nueva Organización**

- **Método:** POST
- **URL:** `{{base_url}}/organizaciones`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "nombre": "Escuela Primaria Nueva",
    "direccion": "Calle Nueva 456, Ciudad D",
    "telefono": "555-2345"
}
```

##### **d. Actualizar una Organización**

- **Método:** PUT
- **URL:** `{{base_url}}/organizaciones/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "nombre": "Escuela Primaria Renovada",
    "direccion": "Calle Renovada 789, Ciudad D",
    "telefono": "555-6789"
}
```

##### **e. Eliminar una Organización**

- **Método:** DELETE
- **URL:** `{{base_url}}/organizaciones/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

---

#### **2. Clases**

##### **a. Obtener Todas las Clases**

- **Método:** GET
- **URL:** `{{base_url}}/clases`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

##### **b. Obtener una Clase por ID**

- **Método:** GET
- **URL:** `{{base_url}}/clases/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

##### **c. Crear una Nueva Clase**

- **Método:** POST
- **URL:** `{{base_url}}/clases`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "nombre": "Cuarto D",
    "organizacion_id": 1
}
```

##### **d. Actualizar una Clase**

- **Método:** PUT
- **URL:** `{{base_url}}/clases/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "nombre": "Quinto E",
    "organizacion_id": 2
}
```

##### **e. Eliminar una Clase**

- **Método:** DELETE
- **URL:** `{{base_url}}/clases/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

##### **f. Obtener Estudiantes de una Clase**

- **Método:** GET
- **URL:** `{{base_url}}/estudiantes/clase/{{clase_id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

**Ejemplo:**

```http
GET http://127.0.0.1:8000/estudiantes/clase/1
```

---

#### **3. Profesores**

##### **a. Obtener Todos los Profesores**

- **Método:** GET
- **URL:** `{{base_url}}/profesores`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

##### **b. Obtener un Profesor por ID**

- **Método:** GET
- **URL:** `{{base_url}}/profesores/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

##### **c. Crear un Nuevo Profesor**

- **Método:** POST
- **URL:** `{{base_url}}/profesores`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "nombre": "José",
    "apellido": "Martínez",
    "email": "jose.martinez@escuela.com",
    "telefono": "555-0004",
    "departamento": "Historia"
}
```

##### **d. Actualizar un Profesor**

- **Método:** PUT
- **URL:** `{{base_url}}/profesores/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "nombre": "José Luis",
    "apellido": "Martínez García",
    "email": "jose.luis.martinez@escuela.com",
    "telefono": "555-0005",
    "departamento": "Geografía"
}
```

##### **e. Eliminar un Profesor**

- **Método:** DELETE
- **URL:** `{{base_url}}/profesores/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

---

#### **4. Asignaturas**

##### **a. Obtener Todas las Asignaturas**

- **Método:** GET
- **URL:** `{{base_url}}/asignaturas`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

##### **b. Obtener una Asignatura por ID**

- **Método:** GET
- **URL:** `{{base_url}}/asignaturas/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

##### **c. Crear una Nueva Asignatura**

- **Método:** POST
- **URL:** `{{base_url}}/asignaturas`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "nombre": "Química",
    "descripcion": "Introducción a la química orgánica",
    "profesor_id": 1
}
```

##### **d. Actualizar una Asignatura**

- **Método:** PUT
- **URL:** `{{base_url}}/asignaturas/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "nombre": "Física",
    "descripcion": "Física avanzada",
    "profesor_id": 2
}
```

##### **e. Eliminar una Asignatura**

- **Método:** DELETE
- **URL:** `{{base_url}}/asignaturas/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

---

#### **5. Administrativos**

##### **a. Obtener Todos los Administrativos**

- **Método:** GET
- **URL:** `{{base_url}}/administrativos`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

##### **b. Obtener un Administrativo por ID**

- **Método:** GET
- **URL:** `{{base_url}}/administrativos/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

##### **c. Crear un Nuevo Administrativo**

- **Método:** POST
- **URL:** `{{base_url}}/administrativos`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "nombre": "Carlos",
    "apellido": "Diaz",
    "email": "carlos.diaz@escuela.com",
    "telefono": "555-1004",
    "puesto": "Director",
    "organizacion_id": 1
}
```

##### **d. Actualizar un Administrativo**

- **Método:** PUT
- **URL:** `{{base_url}}/administrativos/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "nombre": "Carlos Alberto",
    "apellido": "Diaz López",
    "email": "carlos.alberto.diaz@escuela.com",
    "telefono": "555-1005",
    "puesto": "Subdirector",
    "organizacion_id": 2
}
```

##### **e. Eliminar un Administrativo**

- **Método:** DELETE
- **URL:** `{{base_url}}/administrativos/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

---

#### **6. Estudiantes**

##### **a. Obtener Todos los Estudiantes**

- **Método:** GET
- **URL:** `{{base_url}}/estudiantes`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

##### **b. Obtener un Estudiante por ID**

- **Método:** GET
- **URL:** `{{base_url}}/estudiantes/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

##### **c. Crear un Nuevo Estudiante**

- **Método:** POST
- **URL:** `{{base_url}}/estudiantes`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "nombre": "Daniel",
    "apellido": "Ramírez",
    "fecha_nacimiento": "2008-03-22",
    "email": "daniel.ramirez@escuela.com",
    "clase_id": 1
}
```

##### **d. Actualizar un Estudiante**

- **Método:** PUT
- **URL:** `{{base_url}}/estudiantes/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "nombre": "Daniel Alberto",
    "apellido": "Ramírez González",
    "fecha_nacimiento": "2008-03-23",
    "email": "daniel.alberto.ramirez@escuela.com",
    "clase_id": 2
}
```

##### **e. Eliminar un Estudiante**

- **Método:** DELETE
- **URL:** `{{base_url}}/estudiantes/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

---

#### **7. Calificaciones**

##### **a. Obtener Todas las Calificaciones**

- **Método:** GET
- **URL:** `{{base_url}}/calificaciones`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

##### **b. Obtener una Calificación por ID**

- **Método:** GET
- **URL:** `{{base_url}}/calificaciones/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

##### **c. Crear una Nueva Calificación**

- **Método:** POST
- **URL:** `{{base_url}}/calificaciones`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "estudiante_id": 1,
    "asignatura_id": 1,
    "examen": "Examen Parcial",
    "nota": 88.5
}
```

##### **d. Actualizar una Calificación**

- **Método:** PUT
- **URL:** `{{base_url}}/calificaciones/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "estudiante_id": 1,
    "asignatura_id": 1,
    "examen": "Examen Final",
    "nota": 90.0
}
```

##### **e. Eliminar una Calificación**

- **Método:** DELETE
- **URL:** `{{base_url}}/calificaciones/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

---

#### **8. Asistencias**

##### **a. Obtener Todas las Asistencias**

- **Método:** GET
- **URL:** `{{base_url}}/asistencias`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

##### **b. Obtener una Asistencia por ID**

- **Método:** GET
- **URL:** `{{base_url}}/asistencias/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

##### **c. Crear una Nueva Asistencia**

- **Método:** POST
- **URL:** `{{base_url}}/asistencias`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "estudiante_id": 1,
    "fecha": "2024-04-02",
    "presente": true,
    "observaciones": "Llegada puntual"
}
```

##### **d. Actualizar una Asistencia**

- **Método:** PUT
- **URL:** `{{base_url}}/asistencias/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "estudiante_id": 1,
    "fecha": "2024-04-02",
    "presente": false,
    "observaciones": "Enfermedad"
}
```

##### **e. Eliminar una Asistencia**

- **Método:** DELETE
- **URL:** `{{base_url}}/asistencias/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

---

#### **9. Datos Contextuales**

##### **a. Obtener Todos los Datos Contextuales**

- **Método:** GET
- **URL:** `{{base_url}}/datos_contextuales`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

##### **b. Obtener Datos Contextuales por ID**

- **Método:** GET
- **URL:** `{{base_url}}/datos_contextuales/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

##### **c. Crear Datos Contextuales para un Estudiante**

- **Método:** POST
- **URL:** `{{base_url}}/datos_contextuales`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "estudiante_id": 1,
    "sex": "M",
    "age": 16,
    "address": "U",
    "famsize": "LE3",
    "pstatus": "T",
    "medu": 2,
    "fedu": 3,
    "mjob": "teacher",
    "fjob": "health",
    "reason": "reputation",
    "guardian": "mother",
    "traveltime": 2,
    "studytime": 3,
    "failures": 0,
    "schoolsup": true,
    "famsup": true,
    "paid": false,
    "activities": true,
    "nursery": false,
    "higher": true,
    "internet": true,
    "romantic": true,
    "famrel": 4,
    "freetime": 3,
    "goout": 4,
    "dalc": 3,
    "walc": 2,
    "health": 4,
    "absences": 10
}
```

##### **d. Actualizar Datos Contextuales**

- **Método:** PUT
- **URL:** `{{base_url}}/datos_contextuales/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "age": 17,
    "fedu": 4,
    "mjob": "other",
    "reason": "course",
    "famrel": 5,
    "freetime": 5
}
```

##### **e. Eliminar Datos Contextuales**

- **Método:** DELETE
- **URL:** `{{base_url}}/datos_contextuales/{{id}}`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:** N/A

---

### **Resumen de las Llamadas en Postman**

A continuación, se presenta una tabla resumen con todos los endpoints y sus respectivas llamadas:

| Recurso           | Método | Endpoint                                      | Descripción                                         |
|-------------------|--------|-----------------------------------------------|-----------------------------------------------------|
| **Organizaciones**| GET    | `/organizaciones`                             | Obtener todas las organizaciones                    |
|                   | GET    | `/organizaciones/{id}`                        | Obtener una organización por ID                     |
|                   | POST   | `/organizaciones`                             | Crear una nueva organización                        |
|                   | PUT    | `/organizaciones/{id}`                        | Actualizar una organización                         |
|                   | DELETE | `/organizaciones/{id}`                        | Eliminar una organización                          |
| **Clases**        | GET    | `/clases`                                     | Obtener todas las clases                            |
|                   | GET    | `/clases/{id}`                                | Obtener una clase por ID                            |
|                   | POST   | `/clases`                                     | Crear una nueva clase                               |
|                   | PUT    | `/clases/{id}`                                | Actualizar una clase                                |
|                   | DELETE | `/clases/{id}`                                | Eliminar una clase                                  |
|                   | GET    | `/estudiantes/clase/{clase_id}`               | Obtener estudiantes de una clase                    |
| **Profesores**    | GET    | `/profesores`                                 | Obtener todos los profesores                        |
|                   | GET    | `/profesores/{id}`                            | Obtener un profesor por ID                          |
|                   | POST   | `/profesores`                                 | Crear un nuevo profesor                             |
|                   | PUT    | `/profesores/{id}`                            | Actualizar un profesor                              |
|                   | DELETE | `/profesores/{id}`                            | Eliminar un profesor                                |
| **Asignaturas**   | GET    | `/asignaturas`                                | Obtener todas las asignaturas                       |
|                   | GET    | `/asignaturas/{id}`                           | Obtener una asignatura por ID                       |
|                   | POST   | `/asignaturas`                                | Crear una nueva asignatura                          |
|                   | PUT    | `/asignaturas/{id}`                           | Actualizar una asignatura                           |
|                   | DELETE | `/asignaturas/{id}`                           | Eliminar una asignatura                             |
| **Administrativos**| GET   | `/administrativos`                            | Obtener todos los administrativos                   |
|                   | GET    | `/administrativos/{id}`                       | Obtener un administrativo por ID                     |
|                   | POST   | `/administrativos`                            | Crear un nuevo administrativo                       |
|                   | PUT    | `/administrativos/{id}`                       | Actualizar un administrativo                        |
|                   | DELETE | `/administrativos/{id}`                       | Eliminar un administrativo                          |
| **Estudiantes**   | GET    | `/estudiantes`                                | Obtener todos los estudiantes                       |
|                   | GET    | `/estudiantes/{id}`                           | Obtener un estudiante por ID                         |
|                   | POST   | `/estudiantes`                                | Crear un nuevo estudiante                           |
|                   | PUT    | `/estudiantes/{id}`                           | Actualizar un estudiante                            |
|                   | DELETE | `/estudiantes/{id}`                           | Eliminar un estudiante                              |
| **Calificaciones**| GET    | `/calificaciones`                             | Obtener todas las calificaciones                    |
|                   | GET    | `/calificaciones/{id}`                        | Obtener una calificación por ID                      |
|                   | POST   | `/calificaciones`                             | Crear una nueva calificación                        |
|                   | PUT    | `/calificaciones/{id}`                        | Actualizar una calificación                         |
|                   | DELETE | `/calificaciones/{id}`                        | Eliminar una calificación                           |
| **Asistencias**   | GET    | `/asistencias`                                | Obtener todas las asistencias                       |
|                   | GET    | `/asistencias/{id}`                           | Obtener una asistencia por ID                        |
|                   | POST   | `/asistencias`                                | Crear una nueva asistencia                          |
|                   | PUT    | `/asistencias/{id}`                           | Actualizar una asistencia                           |
|                   | DELETE | `/asistencias/{id}`                           | Eliminar una asistencia                             |
| **Datos Contextuales** | GET | `/datos_contextuales`                       | Obtener todos los datos contextuales                |
|                   | GET    | `/datos_contextuales/{id}`                    | Obtener datos contextuales por ID                     |
|                   | POST   | `/datos_contextuales`                         | Crear datos contextuales para un estudiante          |
|                   | PUT    | `/datos_contextuales/{id}`                    | Actualizar datos contextuales                        |
|                   | DELETE | `/datos_contextuales/{id}`                    | Eliminar datos contextuales                          |

---

### **Ejemplo de Llamadas en Postman**

#### **1. Crear una Organización**

- **Método:** POST
- **URL:** `{{base_url}}/organizaciones`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "nombre": "Escuela Primaria Nueva",
    "direccion": "Calle Nueva 456, Ciudad D",
    "telefono": "555-2345"
}
```

#### **2. Obtener Todas las Organizaciones**

- **Método:** GET
- **URL:** `{{base_url}}/organizaciones`
- **Headers:** `Content-Type: application/json`

#### **3. Crear una Clase**

- **Método:** POST
- **URL:** `{{base_url}}/clases`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "nombre": "Primero A",
    "organizacion_id": 1
}
```

#### **4. Crear un Profesor**

- **Método:** POST
- **URL:** `{{base_url}}/profesores`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "nombre": "Juan",
    "apellido": "Pérez",
    "email": "juan.perez@escuela.com",
    "telefono": "555-0001",
    "departamento": "Matemáticas"
}
```

#### **5. Crear una Asignatura**

- **Método:** POST
- **URL:** `{{base_url}}/asignaturas`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "nombre": "Álgebra",
    "descripcion": "Introducción al álgebra básica",
    "profesor_id": 1
}
```

#### **6. Crear un Estudiante**

- **Método:** POST
- **URL:** `{{base_url}}/estudiantes`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "nombre": "Luis",
    "apellido": "Hernández",
    "fecha_nacimiento": "2008-05-15",
    "email": "luis.hernandez@escuela.com",
    "clase_id": 1
}
```

#### **7. Obtener Estudiantes de una Clase**

- **Método:** GET
- **URL:** `{{base_url}}/estudiantes/clase/1`
- **Headers:** `Content-Type: application/json`

#### **8. Crear una Calificación**

- **Método:** POST
- **URL:** `{{base_url}}/calificaciones`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "estudiante_id": 1,
    "asignatura_id": 1,
    "examen": "Examen Parcial",
    "nota": 85.5
}
```

#### **9. Crear una Asistencia**

- **Método:** POST
- **URL:** `{{base_url}}/asistencias`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "estudiante_id": 1,
    "fecha": "2024-04-01",
    "presente": true,
    "observaciones": ""
}
```

#### **10. Crear Datos Contextuales para un Estudiante**

- **Método:** POST
- **URL:** `{{base_url}}/datos_contextuales`
- **Headers:** `Content-Type: application/json`
- **Cuerpo:**

```json
{
    "estudiante_id": 1,
    "sex": "M",
    "age": 16,
    "address": "U",
    "famsize": "LE3",
    "pstatus": "T",
    "medu": 2,
    "fedu": 3,
    "mjob": "teacher",
    "fjob": "health",
    "reason": "reputation",
    "guardian": "mother",
    "traveltime": 2,
    "studytime": 3,
    "failures": 0,
    "schoolsup": true,
    "famsup": true,
    "paid": false,
    "activities": true,
    "nursery": false,
    "higher": true,
    "internet": true,
    "romantic": true,
    "famrel": 4,
    "freetime": 3,
    "goout": 4,
    "dalc": 3,
    "walc": 2,
    "health": 4,
    "absences": 10
}
```

---

### **Importar las Llamadas en Postman**

Para facilitar la prueba, puedes crear una colección en Postman con todas estas solicitudes. Sigue estos pasos:

1. **Abrir Postman.**
2. **Crear una Nueva Colección:**
   - Haz clic en **"New"** y selecciona **"Collection"**.
   - Nombra la colección, por ejemplo, **"Escuela Backend API"**.
3. **Agregar Solicitudes:**
   - Dentro de la colección, agrega cada una de las solicitudes mencionadas anteriormente.
   - Configura los métodos, URLs, headers y cuerpos según se indicó.
4. **Usar Variables:**
   - Asegúrate de usar la variable `{{base_url}}` en las URLs.
5. **Guardar y Organizar:**
   - Guarda cada solicitud y organízalas por recurso para una mejor gestión.

---

### **Consejos Adicionales para Probar con Postman**

1. **Secuencia de Pruebas:**
   - **Crear Recursos:** Primero crea organizaciones, clases, profesores, asignaturas, administrativos y estudiantes.
   - **Crear Relaciones:** Luego, crea calificaciones, asistencias y datos contextuales que dependan de los estudiantes creados.
   - **Obtener y Verificar:** Utiliza los endpoints GET para verificar que los datos se han creado correctamente.
   - **Actualizar y Eliminar:** Prueba los endpoints de actualización y eliminación para asegurarte de que funcionan según lo esperado.

2. **Gestionar IDs Dinámicamente:**
   - Después de crear un recurso (por ejemplo, una organización), toma el `id` de la respuesta y úsalo en solicitudes posteriores que dependan de él.

3. **Manejo de Errores:**
   - Intenta realizar solicitudes con datos inválidos para verificar que la API maneja correctamente los errores (por ejemplo, crear un estudiante con un `clase_id` inexistente).

4. **Documentación Automática:**
   - Utiliza la documentación generada por FastAPI (`/docs`) para entender mejor cada endpoint y probarlos directamente desde allí si lo prefieres.

---

### **Ejemplo de Importación de Colección en Postman (Opcional)**

Si prefieres importar una colección de Postman directamente, puedes crear un archivo JSON con todas las solicitudes. Sin embargo, esto requiere más pasos y configuración manual. Aquí te dejo un ejemplo simplificado de cómo sería una solicitud en JSON para importar:

```json
{
    "info": {
        "name": "Escuela Backend API",
        "_postman_id": "unique-id",
        "description": "Colección para probar los endpoints de la API de Gestión Educativa.",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
    },
    "item": [
        {
            "name": "Obtener Todas las Organizaciones",
            "request": {
                "method": "GET",
                "header": [
                    {
                        "key": "Content-Type",
                        "value": "application/json"
                    }
                ],
                "url": {
                    "raw": "{{base_url}}/organizaciones",
                    "host": ["{{base_url}}"],
                    "path": ["organizaciones"]
                }
            },
            "response": []
        },
        {
            "name": "Crear una Nueva Organización",
            "request": {
                "method": "POST",
                "header": [
                    {
                        "key": "Content-Type",
                        "value": "application/json"
                    }
                ],
                "body": {
                    "mode": "raw",
                    "raw": "{\n    \"nombre\": \"Escuela Primaria Nueva\",\n    \"direccion\": \"Calle Nueva 456, Ciudad D\",\n    \"telefono\": \"555-2345\"\n}"
                },
                "url": {
                    "raw": "{{base_url}}/organizaciones",
                    "host": ["{{base_url}}"],
                    "path": ["organizaciones"]
                }
            },
            "response": []
        }
        // Agrega más solicitudes según sea necesario
    ]
}
```

Para importar esta colección:

1. **Crear un Archivo JSON:**
   - Guarda el contenido anterior en un archivo llamado `Escuela_Backend_API.postman_collection.json`.

2. **Importar en Postman:**
   - Abre Postman.
   - Haz clic en **"Import"**.
   - Selecciona el archivo JSON que creaste.
   - La colección se añadirá a tu lista de colecciones.

**Nota:** Para agregar todas las solicitudes, deberás expandir el JSON con cada endpoint siguiendo el mismo formato.

---

### **Conclusión**

