"""
Inspect Apple's annual revenue records from SEC EDGAR.
"""

import asyncio

from app.providers.sec_financials import SecFinancialsProvider

async def main() -> None:
    """Display recent annual revenue records."""
    provider = SecFinancialsProvider()
    data = await provider.get_company_facts("AAPL")

    if data is None:
        print("Company not found.")
        return

    revenue_fact = data["facts"]["us-gaap"][
        "RevenueFromContractWithCustomerExcludingAssessedTax"
    ]

    print("Label:", revenue_fact["label"])
    print("Description:", revenue_fact["description"])
    print("Available units:", list(revenue_fact["units"]))

    annual_records = provider.get_annual_fact_records(
        data=data,
        fact_name=(
            "RevenueFromContractWithCustomer"
            "ExcludingAssessedTax"
        ),
    )

    print("\nRecent annual records:")

    for record in annual_records[-5:]:
        print(
            {
                "fiscal_year": record.get("fiscal_year"),
                "start": record.get("start"),
                "end": record.get("end"),
                "filed": record.get("filed"),
                "value": record.get("val"),
                "accession": record.get("accn"),
            }
        )

if __name__ == "__main__":
    asyncio.run(main())