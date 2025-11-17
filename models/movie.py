from pydantic import BaseModel, Field
from typing import List

class Movie(BaseModel):
    id: int = Field(alias='movieId', gt=0)
    title: str = Field(..., min_length=1)
    genres: str = Field(..., min_length=1)

    class Config:
        populate_by_name = True