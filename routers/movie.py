# Standar Libraries
from pydantic import BaseModel, Field
from typing import Optional, List

# Project-related libraries (installed via pip)
from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

# Own modules
from config.database import Session
from models.movie import Movie as MovieModel
from middlewares.jwt_bearer import JWTBearer


movie_router = APIRouter()


class Movie(BaseModel):
    """Movie class. Subclass"""
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2023)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_length=6, max_length=20)

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "id": 1,
    #             "title": "Mi película",
    #             "overview": "Descripción de la película",
    #             "year": 2022,
    #             "rating": 9.8,
    #             "category": "Acción"
    #         }
    #     }

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


@movie_router.get('/movies', tags=["movies"], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    """Get movie function"""
    # return movies
    db = Session()
    result = db.query(MovieModel).all()
    # return JSONResponse(status_code=200, content=movies)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movie_router.get('/movies/{id}', tags=["movies"], response_model=Movie)
def get_movie(id: int = Path(ge=1, le=200)) -> Movie:
    """Get movie function"""
    # Sin  base de datos
    # for item in movies:
    #     if item["id"] == id:
    #         return JSONResponse(content=item)
    # return JSONResponse(status_code=404, content=[])
    # Con base de datos
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "Not Found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movie_router.get('/movies/', tags=["movies"], response_model=List[Movie])
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
    # data = [item for item in movies if item['category'] == category]
    # return JSONResponse(content=data)
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.category == category).all()
    if not result:
        return JSONResponse(status_code=404, content={'message': "Not Found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movie_router.post('/movies', tags=["movies"], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    """Function Create movie. Post method."""
    # movies.append(movie.dict())
    # return movies
    db = Session()
    new_movie = MovieModel(**movie.dict())
    db.add(new_movie)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Succesfully Register"})


@movie_router.put('/movies/{id}', tags=["movies"], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> dict:
    """Function update movie. Put method."""
    # for item in movies:
    #     if item["id"] == id:
    #         item["title"] = movie.title
    #         item["overview"] = movie.overview
    #         item["year"] = movie.year
    #         item["rating"] = movie.rating
    #         item["category"] = movie.category
    #         # return movies
    #         return JSONResponse(status_code=200, content={"message": "Se ha modificado la película"})
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "Not Found"})
    result.title = movie.title
    result.overview = movie.overview
    result.year = movie.year
    result.rating = movie.rating
    result.category = movie.category
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Se ha modificado la película"})


@movie_router.delete('/movies/{id}', tags=["movies"], response_model=dict, status_code=200)
def delete_movie(id: int) -> dict:
    """Function update movie. Put method."""
    # for item in movies:
    #     if item["id"] == id:
    #         movies.remove(item)
    #         # return movies
    #         return JSONResponse(status_code=201, content={"message": "Se ha eliminado la película"})
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "Not found"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la película"})