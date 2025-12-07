from pydantic import BaseModel, Field

class Movie(BaseModel):
    id: str = Field(alias='movieId', min_length=1)
    title: str = Field(..., min_length=1)
    genres: str = Field(..., min_length=1)

    class Config:
        populate_by_name = True

class Link(BaseModel):
    movieId: str = Field(...)
    imdbId: str = Field(...)
    tmdbId: str = Field(...)

class Rating(BaseModel):
    userId: str = Field(...)
    movieId: str = Field(...)
    rating: str = Field(...)
    timestamp: str = Field(...)

class Tag(BaseModel):
    userId: str = Field(...)
    movieId: str = Field(...)
    tag: str = Field(...)
    timestamp: str = Field(...)