from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication
from app.schemas.profesor import ProfesorCreate, ProfesorRead, ProfesorUpdate
from app.models.profesor import Profesor
from app.database.connection import get_user_db

SECRET = "SUPERSECRETJWTKEY"

auth_backends = [
    JWTAuthentication(secret=SECRET, lifetime_seconds=3600, tokenUrl="auth/jwt/login")
]

fastapi_users = FastAPIUsers(
    get_user_db,
    auth_backends,
    Profesor,
    ProfesorCreate,
    ProfesorUpdate,
    ProfesorRead,
)

router = APIRouter()

# Incluir las rutas de FastAPI Users
router.include_router(
    fastapi_users.get_auth_router(auth_backends[0]),
    prefix="/auth/jwt",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_register_router(),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_users_router(),
    prefix="/users",
    tags=["users"],
)

@router.post("/login")
def login():
    # TODO: Implementar lógica de inicio de sesión si no se usa FastAPI Users
    pass

@router.post("/register")
def register():
    # TODO: Implementar lógica de registro de usuarios si no se usa FastAPI Users
    pass
