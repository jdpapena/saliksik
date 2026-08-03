"""Provide a database session for each API request."""

from collections.abc import Generator

from sqlalchemy.orm import Session

from app.database import SessionLocal


def get_db() -> Generator[Session, None, None]:
    """Yield one database session and close it afterward."""

    database = SessionLocal()

    try:
        yield database
    finally:
        database.close()