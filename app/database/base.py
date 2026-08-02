"""Shared SQLAlchemy base class.

All database models inherit from Base so SQLAlchemy can track
and create their tables consistently.
"""

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """Parent class for every database model."""

    pass