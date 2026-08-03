"""Fetch the SEC company ticker directory."""

import httpx

from app.core.config import settings

class SecCompanyDirectoryProvider:
    """Retrieve lightweight company records from the SEC."""

    DIRECTORY_URL = (
        "https://www.sec.gov/files/company_tickers_exchange.json"
    )

    def __init__(self) -> None:
        # The SEC asks automated clients to identify themselves.
        self.headers = {
            "User-Agent": settings.sec_user_agent,
        }

    async def get_directory(self) -> dict | None:
        """Download and return the raw SEC company directory."""

        async with httpx.AsyncClient(
            timeout=30.0,
            headers=self.headers,
        ) as client:
            response = await client.get(self.DIRECTORY_URL)

        if response.status_code == 404:
            return None

        response.raise_for_status()

        return response.json()