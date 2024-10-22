# app/auth/users.py

from fastapi_users import FastAPIUsers
from app.models.user import User
from app.auth.manager import get_user_manager
from app.auth.jwt import auth_backend

# Inicializa FastAPIUsers con el tipo de ID correcto (int)
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
