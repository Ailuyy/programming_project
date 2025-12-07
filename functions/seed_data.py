import pandas as pd
import os
import core.config as config
from database.database import SessionLocal, engine, Movie, Link, Rating, Tag, Base

def clean_data(df):
    return df.where(pd.notnull(df), None)

def load_data():
    session = SessionLocal()
    base_path = 'database'
    if not os.path.exists(os.path.join(base_path, 'movies.csv')):
        print("Error: Directory 'database/movies.csv' does not exist!")
        return
    try:
        df_movies = pd.read_csv(os.path.join(base_path, 'movies.csv'))
        movies_data = df_movies.to_dict(orient='records')
        session.bulk_insert_mappings(Movie, movies_data)
        session.commit()
        print(f"Inserted {len(movies_data)} movies to database.")

        df_links = pd.read_csv(os.path.join(base_path, 'links.csv'))
        df_links = clean_data(df_links)

        links_data = df_links.to_dict(orient='records')
        session.bulk_insert_mappings(Link, links_data)
        session.commit()
        print(f"Inserted {len(links_data)} links to database.")

        df_ratings = pd.read_csv(os.path.join(base_path, 'ratings.csv'))
        ratings_data = df_ratings.to_dict(orient='records')
        chunk_size = 10000
        total_ratings = len(ratings_data)

        for i in range(0, total_ratings, chunk_size):
            chunk = ratings_data[i:i + chunk_size]
            session.bulk_insert_mappings(Rating, chunk)
            session.commit()

        print(f"Inserted {len(ratings_data)} ratings to database.")

        df_tags = pd.read_csv(os.path.join(base_path, 'tags.csv'))
        df_tags = clean_data(df_tags)
        tags_data = df_tags.to_dict(orient='records')
        session.bulk_insert_mappings(Tag, tags_data)
        session.commit()
        print(f"Inserted {len(tags_data)} tags to database.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    load_data()