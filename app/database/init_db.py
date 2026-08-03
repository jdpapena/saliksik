"""Create all database tables registered with SQLAlchemy."""

from app.database import Base, engine

# Import each model so SQLAlchemy includes it in the metadata.
from app.models import (
    Company,
    CompanyDirectory,
    ComparisonHistory,
    Dividend,
    FinancialSnapshot,
    HistoricalPrice,
    InvestorProfile,
    NewsRecord,
    SavedCompany,
    User,
)

def create_database() -> None:
    """Create database tables that do not already exist."""

    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_database()
    print("Database created successfully!")