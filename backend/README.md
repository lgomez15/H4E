
## **Escuela Backend API**

![License](https://img.shields.io/badge/license-MIT-blue.svg)

### **Descripción**

**Escuela Backend API** es una API desarrollada con **FastAPI** que gestiona las operaciones de una institución educativa. Permite gestionar organizaciones, clases, profesores, asignaturas, administrativos, estudiantes, calificaciones, asistencias y datos contextuales de los estudiantes. La API está construida utilizando **SQLAlchemy** como ORM y **MariaDB** como sistema de gestión de bases de datos.

### **Características**

- **Gestión de Organizaciones:** Crear, leer, actualizar y eliminar organizaciones educativas.
- **Gestión de Clases:** Administrar clases asociadas a organizaciones.
- **Gestión de Profesores:** Manejar información de profesores y sus asignaturas.
- **Gestión de Asignaturas:** Administrar las asignaturas ofrecidas y sus detalles.
- **Gestión de Administrativos:** Gestionar personal administrativo de la institución.
- **Gestión de Estudiantes:** Crear y gestionar información de estudiantes.
- **Calificaciones y Asistencias:** Registrar y consultar calificaciones y asistencias de los estudiantes.
- **Datos Contextuales:** Almacenar información contextual adicional sobre los estudiantes.

### **Tecnologías Utilizadas**

- **Python 3.12**
- **FastAPI**
- **SQLAlchemy**
- **MariaDB**
- **Alembic** (para migraciones de base de datos)
- **Pydantic**
- **Uvicorn** (servidor ASGI)
- **Git** (control de versiones)

### **Pre-requisitos**

- **Python 3.12** instalado en tu sistema.
- **MariaDB** instalado y ejecutándose.
- **Git** instalado para el control de versiones.

### **Instalación**

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

### **Configuración**

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

### **Ejecutar la Aplicación**

Inicia el servidor de desarrollo con Uvicorn:

```bash
uvicorn app.main:app --reload --log-level debug
```

La API estará disponible en `http://127.0.0.1:8000`.

### **Documentación de la API**

FastAPI genera automáticamente documentación interactiva que puedes acceder en:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### **Uso de la API**

#### **Obtener Todos los Estudiantes de una Clase**

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

### **Estructura del Proyecto**

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

### **Contribución**

¡Contribuciones son bienvenidas! Por favor, sigue estos pasos para contribuir:

1. **Fork** el repositorio.
2. Crea una **rama** para tu feature (`git checkout -b feature/nueva-funcionalidad`).
3. **Commitea** tus cambios (`git commit -m 'Añadir nueva funcionalidad'`).
4. **Push** a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un **Pull Request**.

### **Licencia**

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

### **Contacto**

Para cualquier consulta o sugerencia, por favor, contacta a:

- **Nombre:** Luis García
- **Email:** luis.garcia@ejemplo.com

---

### **Notas Finales**

- **Mantén tu `.gitignore` actualizado** para evitar subir archivos sensibles o innecesarios al repositorio.
- **Realiza pruebas** exhaustivas para asegurarte de que todos los endpoints funcionan correctamente.
- **Actualiza la documentación** conforme añades nuevas funcionalidades o realizas cambios en la estructura de la API.

