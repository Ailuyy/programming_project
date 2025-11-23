import csv
from pathlib import Path
from models.rating import Rating
from typing import List

def get_ratings_from_csv(csv_path: Path) -> List[Rating]:
    ratings = []
    csv_path = Path(csv_path)
    with csv_path.open(encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rating = Rating(
                userId=row["userId"],
                movieId=row["movieId"],
                rating=row["rating"],
                timestamp=row["timestamp"]
            )
            ratings.append(rating)
    return ratings
