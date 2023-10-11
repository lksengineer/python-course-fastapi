# Standar Libraries
from pydantic import BaseModel

# Project-related libraries (installed via pip)
from fastapi import APIRouter
from fastapi.responses import JSONResponse

# Own modules
from jwt_manager import create_token


login_router = APIRouter()


class User(BaseModel):
    """User class. Sub class"""
    email: str
    password: str


@login_router.post('/login', tags=["auth"])
def login(user: User):
    """Login Function"""
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        # token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)
    return JSONResponse(status_code=404, content={"message": "USER NOT FOUND"})
