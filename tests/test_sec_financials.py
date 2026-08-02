"""
Test retrieving Apple financial facts from SEC EDGAR.
"""
import asyncio

from app.providers.sec_financials import SecFinancialsProvider

async def main() -> None:
    """Fetch and inspect Apple XBRL facts."""

    provider = SecFinancialsProvider()
    data = await provider.get_company_facts("AAPL")

    if data is None:
        print("Company not found.")
        return

    print("Entity:", data["entityName"])

    us_gaap = data["facts"].get("us-gaap", {})

    print("Available US-GAAP facts:", len(us_gaap))
    print("Revenue available:", "RevenueFromContractWithCustomerExcludingAssessedTax" in us_gaap)
    print("Net income available:", "NetIncomeLoss" in us_gaap)
    print("Assets available:", "Assets" in us_gaap)

if __name__ == "__main__":
    asyncio.run(main())