from fastapi import FastAPI
from core.config import CSV_FILE_MOVIES, CSV_FILE_LINKS
from functions.get_movies import get_movies_from_csv
from functions.get_links import get_links_from_csv
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/movies")
def get_movies():
    movies = get_movies_from_csv(CSV_FILE_MOVIES)
    return [movie.__dict__ for movie in movies]

@app.get("/links")
def get_links():
    links = get_links_from_csv(CSV_FILE_LINKS)
    return [link.__dict__ for link in links]