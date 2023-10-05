# Standar Libraries
from pydantic import BaseModel, Field
from typing import Optional, List

# Project-related libraries (installed via pip)
from fastapi import FastAPI, Path, Query  # , Body
from fastapi.responses import HTMLResponse, JSONResponse


# app = FastAPI()
# app.title = "My Movie app with FastAPI"
# app.version = "0.0.1"

app = FastAPI(
    title='Aprendiendo FastApi',
    description='An API to learn learning FASTAPI',
    version='0.0.1',
    )


class Movie(BaseModel):
    """Movie class. Subclass"""
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2023)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_length=6, max_length=20)

    model_config = {
        "json_schema_extra": {
             'example': {
                "id": 1,
                "title": "My movie",
                "overview": "Movie Description",
                "year": 2022,
                "rating": 10.0,
                "category": "Acción"
             }
        }
    }


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


@app.get('/movies', tags=["movies"], response_model=List[Movie])
def get_movies() -> List[Movie]:
    """Get movie function"""
    # return movies
    return JSONResponse(content=movies)


@app.get('/movies/{id}', tags=["movies"], response_model=Movie)
def get_movie(id: int = Path(ge=1, le=200)) -> Movie:
    """Get movie function"""
    for item in movies:
        if item["id"] == id:
            return JSONResponse(content=item)
    return JSONResponse(content=[])


@app.get('/movies/', tags=["movies"], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=6, max_length=20)) -> List[Movie]:
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
    # return [item for item in movies if item['category'] == category]
    data = [item for item in movies if item['category'] == category]
    return JSONResponse(content=data)


@app.post('/movies', tags=["movies"], response_model=dict)
def create_movie(movie: Movie) -> dict:
    """Function Create movie. Post method."""
    movies.append(movie)
    # return movies
    return JSONResponse(content={"message": "Succesfully Register"})


@app.put('/movies/{id}', tags=["movies"], response_model=dict)
def update_movie(id: int, movie: Movie) -> dict:
    """Function update movie. Put method."""
    for item in movies:
        if item["id"] == id:
            item["title"] = movie.title
            item["overview"] = movie.overview
            item["year"] = movie.year
            item["rating"] = movie.rating
            item["category"] = movie.category
            # return movies
            return JSONResponse(content={"message": "Se ha modificado la película"})


@app.delete('/movies/{id}', tags=["movies"], response_model=dict)
def delete_movie(id: int) -> dict:
    """Function update movie. Put method."""
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            # return movies
            return JSONResponse(content={"message": "Se ha eliminado la película"})
