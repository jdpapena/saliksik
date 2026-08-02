"""
Retrieves structured XBRL financial facts for one US company.
"""

import httpx

from app.core.config import settings
from app.providers.sec_edgar import SecEdgarProvider
from datetime import date

class SecFinancialsProvider:

    """Retrieve company financial facts from SEC EDGAR."""
    BASE_URL = "https://data.sec.gov/api/xbrl/companyfacts"

    def _headers(self) -> dict[str, str]:
        """Return headers required for SEC requests."""

        return {
            "User-Agent": settings.sec_user_agent,
            "Accept-Encoding": "gzip, deflate",
        }

    async def get_company_facts(
        self,
        ticker: str,
    ) -> dict | None:

        company_provider = SecEdgarProvider()
        cik = await company_provider.get_cik(ticker)

        if cik is None:
            return None

        url = f"{self.BASE_URL}/CIK{cik}.json"

        async with httpx.AsyncClient(
            headers=self._headers(),
            timeout=30.0,
        ) as client:
            response = await client.get(url)
            response.raise_for_status()

        return response.json()

    def get_annual_fact_records(
        self,
        data: dict,
        fact_name: str,
        unit: str = "USD",
        duration_fact: bool = False,
    ) -> list[dict]:
        """Return deduplicated annual records for one SEC fact."""

        fact = data["facts"]["us-gaap"].get(fact_name)

        if fact is None:
            return []

        records = fact["units"].get(unit, [])

        annual_records = [
            record
            for record in records
            if record.get("form") == "10-K"
            and record.get("fp") == "FY"
            and record.get("end")
        ]

        if duration_fact:
            annual_records = [
                record
                for record in annual_records
                if record.get("start")
                and 300
                <= (
                    date.fromisoformat(record["end"])
                    - date.fromisoformat(record["start"])
                ).days
                <= 380
            ]

        records_by_end_date: dict[str, dict] = {}

        for record in annual_records:
            end_date = record["end"]
            existing = records_by_end_date.get(end_date)

            if (
                existing is None
                or record.get("filed", "") > existing.get("filed", "")
            ):
                records_by_end_date[end_date] = record

        sorted_records = sorted(
            records_by_end_date.values(),
            key=lambda record: record["end"],
        )

        for record in sorted_records:
            record["fiscal_year"] = int(record["end"][:4])

        return sorted_records