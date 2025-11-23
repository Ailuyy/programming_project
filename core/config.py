from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = BASE_DIR / "database"
CSV_FILE_MOVIES = BASE_DIR / "movies.csv"
CSV_FILE_LINKS = BASE_DIR / "links.csv"
CSV_FILE_RATINGS = BASE_DIR / "ratings.csv"
CSV_FILE_TAGS = BASE_DIR / "tags.csv"