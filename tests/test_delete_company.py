from app.database import SessionLocal
from app.services.company_service import (
    create_company,
    delete_company,
    get_company_by_ticker,
)

database = SessionLocal()

try:
    # Create a temporary company so we don't delete Apple.
    company = create_company(
        database=database,
        ticker="TEST",
        name="Test Company",
        exchange="TEST",
        country="Test Country",
        sector="Testing",
        industry="Testing",
        description="Temporary company used for testing.",
        website="https://example.com",
        market_cap=1,
        currency="USD",
        employees=1,
    )

    print("Created:", company.ticker)

    delete_company(
        database,
        company,
    )

    company = get_company_by_ticker(
        database,
        "TEST",
    )

    print("Deleted:", company is None)

finally:
    database.close()