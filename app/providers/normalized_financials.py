"""
Defines the financial format used internally by SALIKSIK.
"""
from dataclasses import dataclass
from datetime import date
from decimal import Decimal

@dataclass
class NormalizedFinancialSnapshot:
    """Raw financial facts for one reporting period."""

    fiscal_year: int
    fiscal_period: str
    report_date: date
    filing_date: date | None
    currency: str | None

    revenue: Decimal | None = None
    gross_profit: Decimal | None = None
    operating_income: Decimal | None = None
    net_income: Decimal | None = None
    earnings_per_share: Decimal | None = None

    cash_and_equivalents: Decimal | None = None
    current_assets: Decimal | None = None
    total_assets: Decimal | None = None
    current_liabilities: Decimal | None = None
    total_liabilities: Decimal | None = None
    total_debt: Decimal | None = None
    shareholders_equity: Decimal | None = None
    shares_outstanding: Decimal | None = None

    operating_cash_flow: Decimal | None = None
    capital_expenditure: Decimal | None = None