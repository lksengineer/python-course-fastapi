# Standar Libraries
from pydantic import BaseModel


class User(BaseModel):
    """User class. Sub class"""
    email: str
    password: str
