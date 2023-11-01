# Own modules.
from models.movie import Movie as MovieModel
from schemas.movie import Movie


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

    def create_movie(self, movie: Movie):
        """Create movie method."""
        new_movie = MovieModel(**movie.model_dump())
        self.db.add(new_movie)
        self.db.commit()
        return

    def update_movie(self, id: int, data: Movie):
        """Update movie method."""
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.rating
        movie.category = data.category
        self.db.commit()
        return
