import csv
from pathlib import Path
from models.link import Link
from typing import List

def get_links_from_csv(csv_path: Path) -> List[Link]:
    links = []
    csv_path = Path(csv_path)
    with csv_path.open(encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            link = Link(
                movieId=row["movieId"],
                imdbId=row["imdbId"],
                tmdbId=row["tmdbId"]
            )
            links.append(link)
    return links
