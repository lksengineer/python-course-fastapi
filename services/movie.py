# Own modules.
from models.movie import Movie as MovieModel


class MovieService():
    """Class Movie service."""
    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        """Get movies method."""
        result = self.db.query(MovieModel).all()
        return result

    def get_movie(self, id):
        """Get movie method."""
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result

    def get_movies_by_category(self, category):
        """Get category method."""
        result = self.db.query(MovieModel).filter(MovieModel.category == category).all()
        return result
