import csv
from pathlib import Path
from models.movie import Movie
from typing import List

def get_movies_from_csv(csv_path: Path) -> List[Movie]:
    movies = []
    csv_path = Path(csv_path)
    with csv_path.open(encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            movie = Movie(
                movieId=int(row["movieId"]),
                title=row["title"],
                genres=row["genres"].split('|')
            )
            movies.append(movie)
    return movies
