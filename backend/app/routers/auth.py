from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend, BearerTransport
from fastapi_users.authentication.strategy import JWTStrategy
from app.schemas.profesor import ProfesorCreate, ProfesorRead, ProfesorUpdate
from app.models.profesor import Profesor
from app.database.connection import get_db

SECRET = "SUPERSECRETJWTKEY"

# Define the JWT strategy
def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

# Define the transport method (Bearer token)
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

# Define the authentication backend
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

# Initialize FastAPI Users
fastapi_users = FastAPIUsers(
    get_db,
    [auth_backend],
    Profesor,
    ProfesorCreate,
    ProfesorUpdate,
    ProfesorRead,
)

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

# Include the routes of FastAPI Users
router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_register_router(),
    prefix="/",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_users_router(),
    prefix="/users",
    tags=["users"],
)
