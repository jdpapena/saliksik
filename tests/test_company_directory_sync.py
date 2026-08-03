"""
Test synchronizing the SEC company directory.
"""

import asyncio

from app.database import SessionLocal
from app.services.company_directory_service import (
    sync_sec_company_directory,
)

async def main() -> None:
    database = SessionLocal()

    try:
        saved_count = await sync_sec_company_directory(
            database=database,
        )

        print("Directory records saved:", saved_count)
    finally:
        database.close()

if __name__ == "__main__":
    asyncio.run(main())