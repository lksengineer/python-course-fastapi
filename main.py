# Project-related libraries (installed via pip)
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def message():
    return "Hello World!"
