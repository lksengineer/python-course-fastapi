# Project-related libraries (installed via pip)
from fastapi import FastAPI, Body
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


@app.get('/movies', tags=["movies"])
def get_movies():
    """Get movie function"""
    return movies


@app.get('/movies/{id}', tags=["movies"])
def get_movie(id: int):
    """Get movie function"""
    for item in movies:
        if item["id"] == id:
            return item
    return []


@app.get('/movies/', tags=["movies"])
def get_movies_by_category(category: str, year: int):
    """Function Get movies by category"""
    # return category, year
    # for item in movies:
    #     if item["category"] == category:
    #         return item
    # return []

    # # My Solution
    # movie = list(filter(lambda item: item["category"] == category, movies))
    # return movie if len(movie) > 0 else []

    # Solution of the teacher
    return [item for item in movies if item['category'] == category]


@app.post('/movies', tags=["movies"])
def create_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    """Function Create movie."""
    movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
        })
    return movies
