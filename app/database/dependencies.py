"""
Provides one database session for each API request, then closes it safely after the request finishes.
"""

from collections.abc import Generator

from sqlalchemy.orm import Session

from app.database import SessionLocal

def get_db() -> Generator[Session, None, None]:
    """Yield a database session and close it afterward."""

    database = SessionLocal()

    try:
        yield database
    finally:
        database.close()