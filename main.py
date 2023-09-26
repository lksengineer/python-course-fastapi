# Project-related libraries (installed via pip)
from fastapi import FastAPI


app = FastAPI()
app.title = "My Movie app with FastAPI"
app.version = "0.0.1"


@app.get('/', tags=["home"])
def message():
    return "Hello World!"
