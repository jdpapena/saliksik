"""Define the shared SQLAlchemy base class."""

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """Parent class inherited by every database model."""