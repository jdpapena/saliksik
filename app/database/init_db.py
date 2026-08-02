"""
Creates all database tables defined in the SQLAlchemy models.
"""

# Local imports
from app.database import Base, engine

# Import all models so SQLAlchemy knows they exist.
from app.models import (
    Company,
    FinancialSnapshot,
    HistoricalPrice,
    Dividend,
    NewsRecord,
    User,
    InvestorProfile,
    SavedCompany,
    ComparisonHistory,
)

def create_database() -> None:
    """Create all database tables."""
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_database()
    print("Database created successfully!")