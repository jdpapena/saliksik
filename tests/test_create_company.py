from app.database import SessionLocal
from app.services.company_service import create_company

database = SessionLocal()

try:
    company = create_company(
        database=database,
        ticker="AAPL",
        name="Apple Inc.",
        exchange="NASDAQ",
        country="United States",
        sector="Technology",
        industry="Consumer Electronics",
        description="Apple designs and sells consumer technology products.",
        website="https://www.apple.com",
        market_cap=3_000_000_000_000,
        currency="USD",
        employees=164_000,
    )

    print(company.id)
    print(company.ticker)
    print(company.name)
finally:
    database.close()