from pydantic import BaseModel, Field

class Movie(BaseModel):
    id: str = Field(alias='movieId', min_length=1)
    title: str = Field(..., min_length=1)
    genres: str = Field(..., min_length=1)

    class Config:
        populate_by_name = True