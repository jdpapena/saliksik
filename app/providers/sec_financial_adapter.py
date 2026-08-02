"""
Convert SEC XBRL data into SALIKSIK financial snapshots.
"""

from datetime import date
from decimal import Decimal

from app.providers.normalized_financials import (
    NormalizedFinancialSnapshot,
)
from app.providers.sec_financials import SecFinancialsProvider

FACT_MAP = {
    "revenue": (
        ["RevenueFromContractWithCustomerExcludingAssessedTax"],
        "USD",
        True,
    ),
    "gross_profit": (
        ["GrossProfit"],
        "USD",
        True,
    ),
    "operating_income": (
        ["OperatingIncomeLoss"],
        "USD",
        True,
    ),
    "net_income": (
        ["NetIncomeLoss"],
        "USD",
        True,
    ),
    "earnings_per_share": (
        ["EarningsPerShareDiluted"],
        "USD/shares",
        True,
    ),
    "cash_and_equivalents": (
        [
            "CashAndCashEquivalentsAtCarryingValue",
            "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents",
        ],
        "USD",
        False,
    ),
    "current_assets": (
        ["AssetsCurrent"],
        "USD",
        False,
    ),
    "total_assets": (
        ["Assets"],
        "USD",
        False,
    ),
    "current_liabilities": (
        ["LiabilitiesCurrent"],
        "USD",
        False,
    ),
    "total_liabilities": (
        ["Liabilities"],
        "USD",
        False,
    ),
    "shareholders_equity": (
        ["StockholdersEquity"],
        "USD",
        False,
    ),
    "shares_outstanding": (
        ["EntityCommonStockSharesOutstanding"],
        "shares",
        False,
    ),
    "operating_cash_flow": (
        ["NetCashProvidedByUsedInOperatingActivities"],
        "USD",
        True,
    ),
    "capital_expenditure": (
        ["PaymentsToAcquirePropertyPlantAndEquipment"],
        "USD",
        True,
    ),
}


class SecFinancialAdapter:

    """Normalize SEC financial facts for SALIKSIK."""
    def __init__(self) -> None:
        self.provider = SecFinancialsProvider()

    def _find_records(
        self,
        data: dict,
        fact_names: list[str],
        unit: str,
        duration_fact: bool,
    ) -> list[dict]:
        
        """Return records using the first available SEC fact name."""
        for fact_name in fact_names:
            records = self.provider.get_annual_fact_records(
                data=data,
                fact_name=fact_name,
                unit=unit,
                duration_fact=duration_fact,
            )

            if records:
                return records

        return []

    def normalize(
        self,
        data: dict,
    ) -> list[NormalizedFinancialSnapshot]:
        
        """Convert SEC data into provider-independent snapshots."""
        values_by_year: dict[int, dict] = {}

        for field_name, (
            fact_names,
            unit,
            duration_fact,
        ) in FACT_MAP.items():
            records = self._find_records(
                data=data,
                fact_names=fact_names,
                unit=unit,
                duration_fact=duration_fact,
            )

            for record in records:
                fiscal_year = record["fiscal_year"]

                year_values = values_by_year.setdefault(
                    fiscal_year,
                    {
                        "fiscal_year": fiscal_year,
                        "fiscal_period": "FY",
                        "report_date": date.fromisoformat(record["end"]),
                        "filing_date": (
                            date.fromisoformat(record["filed"])
                            if record.get("filed")
                            else None
                        ),
                        "currency": "USD",
                    },
                )

                year_values[field_name] = Decimal(
                    str(record["val"])
                )

        return [
            NormalizedFinancialSnapshot(**values)
            for _, values in sorted(values_by_year.items())
        ]