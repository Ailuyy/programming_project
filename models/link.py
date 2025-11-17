from pydantic import BaseModel, Field

class Link(BaseModel):
    movieId: str = Field(...)
    imdbId: str = Field(...)
    tmdbId: str = Field(...)