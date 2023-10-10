# Project-related libraries (installed via pip)
from sqlalchemy import Column, Integer, String, Float

# Own modules
from config.database import Base


class Movie(Base):
    """Movie class."""
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)
