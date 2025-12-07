from sqlalchemy import create_engine, Float, ForeignKey, String
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker

class Base(DeclarativeBase):
    pass

class Movie(Base):
    __tablename__ = 'movies'

    movieId: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    genres: Mapped[str]
    links: Mapped['Link'] = relationship('Link', back_populates='movie', uselist=False, cascade='all, delete-orphan')
    ratings: Mapped[list['Rating']] = relationship('Rating', back_populates='movie', cascade='all, delete-orphan')
    tags: Mapped[list['Tag']] = relationship('Tag', back_populates='movie', cascade='all, delete-orphan')

    def __repr__(self) -> str:
        return f'Movie(movieId={self.movieId}, title={self.title}), genres={self.genres}'


class Link(Base):
    __tablename__ = 'links'

    movieId: Mapped[int] = mapped_column(ForeignKey('movies.movieId'), primary_key=True)
    imdbId: Mapped[str] = mapped_column(String)
    tmdbId: Mapped[Optional[float]] = mapped_column(Float, nullable=True)

    movie: Mapped["Movie"] = relationship(back_populates="links")

    def __repr__(self) -> str:
        return f'Link(movieId={self.movieId}, imdbId={self.imdbId})'

class Rating(Base):
    __tablename__ = 'ratings'
    userId: Mapped[int] = mapped_column(primary_key=True)
    movieId: Mapped[int] = mapped_column(ForeignKey('movies.movieId'), primary_key=True)
    rating: Mapped[float]
    timestamp: Mapped[int]

    movie: Mapped["Movie"] = relationship(back_populates="ratings")

    def __repr__(self) -> str:
        return f'Rating(movieId={self.movieId}, rating={self.rating}, timestamp={self.timestamp})'

class Tag(Base):
    __tablename__ = 'tags'

    userId: Mapped[int] = mapped_column(primary_key=True)
    movieId: Mapped[int] = mapped_column(ForeignKey('movies.movieId'), primary_key=True)
    tag: Mapped[str] = mapped_column(String, primary_key=True)
    timestamp: Mapped[int]

    movie: Mapped["Movie"] = relationship(back_populates="tags")

    def __repr__(self) -> str:
        return f'Tag(movieId={self.movieId}, tag={self.tag})'

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

engine = create_engine("sqlite:///programming_project.db", echo=True)
SessionLocal = sessionmaker(bind=engine)