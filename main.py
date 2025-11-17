from fastapi import FastAPI
from core.config import CSV_FILE
from functions.get_movies import get_movies_from_csv
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/movies")
def get_movies():
    movies = get_movies_from_csv(CSV_FILE)
    return [movie.__dict__ for movie in movies]