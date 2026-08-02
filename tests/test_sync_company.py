"""
Test saving official SEC company information.
"""

import asyncio

from app.database import SessionLocal
from app.services.sync_service import sync_company_from_sec

async def main() -> None:
    """Synchronize Apple and display the saved result."""

    database = SessionLocal()

    try:
        company = await sync_company_from_sec(
            database=database,
            ticker="AAPL",
        )

        if company is None:
            print("Company not found.")
            return

        print("ID:", company.id)
        print("Ticker:", company.ticker)
        print("Name:", company.name)
        print("Exchange:", company.exchange)
        print("Industry:", company.industry)

    finally:
        database.close()

if __name__ == "__main__":
    asyncio.run(main())