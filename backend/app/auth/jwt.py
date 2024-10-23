from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Leer la clave secreta del archivo .env
SECRET = os.getenv("SECRET_KEY")

if not SECRET:
    raise ValueError("La variable de entorno 'SECRET_KEY' no está definida.")

bearer_transport = BearerTransport(tokenUrl="/auth/jwt/login")  # Asegúrate de que el tokenUrl es correcto

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
