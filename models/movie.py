from pydantic import BaseModel, Field
from typing import List

class Movie(BaseModel):
    movieId: int = Field(..., gt=0)
    title: str = Field(..., min_length=1)
    genres: List[str] = []
