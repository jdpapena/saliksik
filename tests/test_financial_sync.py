"""
Test syncing annual Apple financial facts.
"""

import asyncio

from app.database import SessionLocal
from app.services.financial_sync_service import (
    sync_annual_financials_from_sec,
)

async def main() -> None:
    database = SessionLocal()

    try:
        snapshots = await sync_annual_financials_from_sec(
            database=database,
            ticker="AAPL",
        )

        latest = max(
            snapshots,
            key=lambda snapshot: snapshot.fiscal_year,
        )

        print("Fiscal year:", latest.fiscal_year)
        print("Revenue:", latest.revenue)
        print("Net income:", latest.net_income)
        print("Assets:", latest.total_assets)
    finally:
        database.close()

if __name__ == "__main__":
    asyncio.run(main())