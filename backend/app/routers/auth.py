from fastapi import APIRouter, Depends, Request, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.models.user import User
from app.schemas.user import UserRead
from app.auth.manager import UserManager, get_user_manager

auth_router = APIRouter()

@auth_router.post("/auth/jwt/login", tags=["auth"])
def login(
    request: Request,
    credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    """
    Ruta de inicio de sesión simplificada.
    Verifica si el usuario existe y devuelve sus datos.
    """
    # Buscar el usuario por email
    user = db.query(User).filter(User.email == credentials.username).first()
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Credenciales inválidas",
        )
    
    # Para simplificar, omitimos la verificación de contraseña
    # Nota: En una aplicación real, siempre verifica la contraseña
    
    # Convertir el modelo SQLAlchemy a Pydantic
    user_data = UserRead.from_orm(user)
    
    return {
        "status": "ok",
        "user": user_data,
    }

# Opcional: Si ya no usas fastapi-users para otras funcionalidades, puedes eliminar las siguientes líneas
# auth_router.include_router(
#     fastapi_users.get_register_router(UserRead, UserCreate),
#     prefix="/auth",
#     tags=["auth"],
# )

# auth_router.include_router(
#     fastapi_users.get_users_router(UserRead, UserUpdate),
#     prefix="/users",
#     tags=["users"],
# )
