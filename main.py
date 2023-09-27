# Project-related libraries (installed via pip)
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


# app = FastAPI()
# app.title = "My Movie app with FastAPI"
# app.version = "0.0.1"

app = FastAPI(
    title='Aprendiendo FastApi',
    description='An API to learn learning FASTAPI',
    version='0.0.1',
    )

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    }
]


@app.get('/', tags=["home"])
def message():
    return HTMLResponse("<h1>Hello world!</h1>")
    # return {"name": "Luis", "last_name": "Saavedra", "age": 33}


@app.get('/movie', tags=["movies"])
def get_movie():
    return movies
