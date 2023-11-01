# Standar Libraries
from pydantic import BaseModel, Field
from typing import Optional


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
