import csv
from pathlib import Path
from models.tag import Tag
from typing import List

def get_tags_from_csv(csv_path: Path) -> List[Tag]:
    tags = []
    csv_path = Path(csv_path)
    with csv_path.open(encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            tag = Tag(
                userId=row["userId"],
                movieId=row["movieId"],
                tag=row["tag"],
                timestamp=row["timestamp"]
            )
            tags.append(tag)
    return tags
