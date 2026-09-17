from sqlalchemy.orm import sessionmaker

from database.connection import engine

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
from sqlalchemy.orm import Session


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()