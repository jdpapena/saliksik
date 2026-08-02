from app.database import SessionLocal
from app.services.company_service import (
    get_company_by_ticker,
    update_company,
)

database = SessionLocal()

try:
    company = get_company_by_ticker(
        database,
        "AAPL",
    )

    if company is None:
        print("Company not found.")
    else:
        update_company(
            database,
            company,
            employees=170000,
        )

        print(company.name)
        print(company.employees)

finally:
    database.close()