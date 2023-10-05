# Project-related libraries (installed via pip)
from jwt import encode, decode


def create_token(data: dict):
    """Function create token."""
    token: str = encode(payload=data, key="my_secrete_key", algorithm="HS256")
    return token


def validate_token(token: str) -> dict:
    """Function validate token."""
    data: dict = decode(token, key="my_secret_key", algorithms=['HS256'])
    return data
