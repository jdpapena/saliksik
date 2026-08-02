"""
Resolves a US stock ticker to its SEC CIK, then retrieves
official company submission information from SEC EDGAR.
"""

import httpx

from app.core.config import settings


class SecEdgarProvider:
    """Retrieve official US company information from SEC EDGAR."""
    TICKER_URL = "https://www.sec.gov/files/company_tickers.json"
    SUBMISSIONS_URL = "https://data.sec.gov/submissions"

    def _headers(self) -> dict[str, str]:

        return {
            "User-Agent": settings.sec_user_agent,
            "Accept-Encoding": "gzip, deflate",
        }

    async def get_cik(self, ticker: str) -> str | None:
        """Return the ten-digit SEC CIK for a stock ticker."""
        async with httpx.AsyncClient(headers=self._headers()) as client:
            response = await client.get(self.TICKER_URL)
            response.raise_for_status()

        companies = response.json()
        normalized_ticker = ticker.upper()

        for company in companies.values():
            if company["ticker"].upper() == normalized_ticker:
                return str(company["cik_str"]).zfill(10)

        return None

    async def get_company_submissions(
        self,
        ticker: str,
    ) -> dict | None:
        """Return official SEC submission data for one ticker."""
        cik = await self.get_cik(ticker)

        if cik is None:
            return None

        url = f"{self.SUBMISSIONS_URL}/CIK{cik}.json"

        async with httpx.AsyncClient(headers=self._headers()) as client:
            response = await client.get(url)
            response.raise_for_status()

        return response.json()