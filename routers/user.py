# Standar Libraries

# Project-related libraries (installed via pip)
from fastapi import APIRouter
from fastapi.responses import JSONResponse

# Own modules
from jwt_manager import create_token
from schemas.user import User

user_router = APIRouter()


@user_router.post('/login', tags=["auth"])
def login(user: User):
    """Login Function"""
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.model_dump())
        # token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)
    return JSONResponse(status_code=404, content={"message": "USER NOT FOUND"})
