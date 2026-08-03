"""
Fetch the SEC's searchable company ticker directory.
"""

import httpx

class SecCompanyDirectoryProvider:
    """Retrieve lightweight company-directory records from SEC."""
    DIRECTORY_URL = (
        "https://www.sec.gov/files/company_tickers_exchange.json"
    )

    def __init__(self) -> None:
        self.headers = {
            "User-Agent": (
                "SALIKSIK contact@example.com"
            )
        }

    async def get_directory(self) -> dict | None:
        async with httpx.AsyncClient(
            timeout=30.0,
            headers=self.headers,
        ) as client:
            response = await client.get(self.DIRECTORY_URL)

        if response.status_code == 404:
            return None

        response.raise_for_status()
        return response.json()