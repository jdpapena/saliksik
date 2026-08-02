"""Test reading companies from the database."""

from app.database import SessionLocal
from app.services.company_service import (
    get_all_companies,
    get_company_by_ticker,
)

database = SessionLocal()

try:
    print("----- One Company -----")

    company = get_company_by_ticker(
        database,
        "AAPL",
    )

    print(company.ticker)
    print(company.name)

    print()

    print("----- All Companies -----")

    companies = get_all_companies(database)

    for company in companies:
        print(company.ticker, "-", company.name)

finally:
    database.close()