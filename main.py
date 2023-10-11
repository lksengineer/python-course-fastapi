# Project-related libraries (installed via pip)
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Own modules
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.login import login_router


# app = FastAPI()
# app.title = "My Movie app with FastAPI"
# app.version = "0.0.1"

app = FastAPI(
    title='Aprendiendo FastApi',
    description='An API to learn learning FASTAPI',
    version='0.0.1',
    )

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(login_router)

Base.metadata.create_all(bind=engine)

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    }
]


@app.get('/', tags=["home"])
def message():
    """Message function"""
    return HTMLResponse("<h1>Hello world!</h1>")
    # return {"name": "Luis", "last_name": "Saavedra", "age": 33}
