from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database.database import get_db, Movie, Link, Rating, Tag
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/movies")
def get_movies(db: Session = Depends(get_db)):
    return db.query(Movie).all()

@app.get("/links")
def get_links(db: Session = Depends(get_db)):
    return db.query(Link).all()

@app.get("/ratings")
def get_ratings(db: Session = Depends(get_db)):
    return db.query(Rating).all()

@app.get("/tags")
def get_tags(db: Session = Depends(get_db)):
    return db.query(Tag).all()