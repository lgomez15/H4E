# app/auth/manager.py

from fastapi_users.manager import BaseUserManager, IntegerIDMixin
from app.models.user import User
from app.auth.jwt import SECRET
from fastapi import Request, Depends
from typing import Optional
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from app.database.connection import get_user_db  # Asegúrate de que esta importación es correcta

class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"Usuario registrado: {user.id}")

    def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Usuario olvidó la contraseña: {user.id}, token: {token}")

def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)
