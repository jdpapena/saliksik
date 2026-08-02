"""
Pydantic schemas for company comparisons.
"""

from datetime import date
from decimal import Decimal

from pydantic import BaseModel

class MetricComparison(BaseModel):
    id: str
    metric: str
    definition: str
    formula: str
    why_it_matters: str
    things_to_consider: str

    company_a_value: Decimal | None
    company_b_value: Decimal | None
    unit: str

class CompanyComparisonResponse(BaseModel):
    """Factual comparison between two companies."""
    ticker_a: str
    name_a: str
    report_date_a: date

    ticker_b: str
    name_b: str
    report_date_b: date

    fiscal_year: int
    metrics: list[MetricComparison]
    