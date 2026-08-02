"""
Pydantic schemas for financial snapshot responses.
"""

from datetime import date
from decimal import Decimal

from pydantic import BaseModel, ConfigDict

class FinancialSnapshotResponse(BaseModel):
    """Annual financial facts returned by the API."""

    model_config = ConfigDict(from_attributes=True)

    fiscal_year: int
    fiscal_period: str
    report_date: date
    filing_date: date | None
    currency: str | None

    revenue: Decimal | None
    gross_profit: Decimal | None
    operating_income: Decimal | None
    net_income: Decimal | None
    earnings_per_share: Decimal | None

    cash_and_equivalents: Decimal | None
    current_assets: Decimal | None
    total_assets: Decimal | None
    current_liabilities: Decimal | None
    total_liabilities: Decimal | None
    total_debt: Decimal | None
    shareholders_equity: Decimal | None
    shares_outstanding: Decimal | None

    operating_cash_flow: Decimal | None
    capital_expenditure: Decimal | None