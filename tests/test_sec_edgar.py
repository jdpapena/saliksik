"""
Test the SEC EDGAR provider with Apple.
"""

import asyncio

from app.providers.sec_edgar import SecEdgarProvider

async def main() -> None:
    """Fetch Apple data from SEC EDGAR."""
    provider = SecEdgarProvider()

    cik = await provider.get_cik("AAPL")
    print("CIK:", cik)

    company = await provider.get_company_submissions("AAPL")

    if company is None:
        print("Company not found.")
        return

    print("Name:", company["name"])
    print("Tickers:", company["tickers"])
    print("Exchanges:", company["exchanges"])
    print("SIC description:", company["sicDescription"])

if __name__ == "__main__":
    asyncio.run(main())