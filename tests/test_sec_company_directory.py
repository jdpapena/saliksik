"""
Inspect the SEC company-directory response.
"""

import asyncio

from app.providers.sec_company_directory import (
    SecCompanyDirectoryProvider,
)

async def main() -> None:
    provider = SecCompanyDirectoryProvider()
    data = await provider.get_directory()

    if data is None:
        print("Directory not found.")
        return

    print("Fields:", data.get("fields"))
    print("Total records:", len(data.get("data", [])))

    for record in data.get("data", [])[:5]:
        print(record)

if __name__ == "__main__":
    asyncio.run(main())