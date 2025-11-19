from pydantic import BaseModel, Field

class Rating(BaseModel):
    userId: str = Field(...)
    movieId: str = Field(...)
    rating: str = Field(...)
    timestamp: str = Field(...)