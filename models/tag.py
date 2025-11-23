from pydantic import BaseModel, Field

class Tag(BaseModel):
    userId: str = Field(...)
    movieId: str = Field(...)
    tag: str = Field(...)
    timestamp: str = Field(...)