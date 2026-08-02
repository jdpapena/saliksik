"""
Business logic for comparing company financial facts.
"""

from sqlalchemy.orm import Session

from app.models.company import Company
from app.models.financial_snapshot import FinancialSnapshot
from app.education.metrics import METRIC_DEFINITIONS

COMPARISON_FIELDS = {
    "revenue": ("Revenue", "USD"),
    "gross_profit": ("Gross Profit", "USD"),
    "operating_income": ("Operating Income", "USD"),
    "net_income": ("Net Income", "USD"),
    "earnings_per_share": ("Diluted Earnings per Share", "USD/share"),
    "cash_and_equivalents": ("Cash and Cash Equivalents", "USD"),
    "current_assets": ("Current Assets", "USD"),
    "total_assets": ("Total Assets", "USD"),
    "current_liabilities": ("Current Liabilities", "USD"),
    "total_liabilities": ("Total Liabilities", "USD"),
    "shareholders_equity": ("Shareholders' Equity", "USD"),
    "operating_cash_flow": ("Operating Cash Flow", "USD"),
    "capital_expenditure": ("Capital Expenditure", "USD"),
}

def compare_companies(
    database: Session,
    company_a: Company,
    company_b: Company,
) -> dict | None:
    
    """Compare companies using their latest shared fiscal year."""
    snapshots_a = (
        database.query(FinancialSnapshot)
        .filter(FinancialSnapshot.company_id == company_a.id)
        .all()
    )

    snapshots_b = (
        database.query(FinancialSnapshot)
        .filter(FinancialSnapshot.company_id == company_b.id)
        .all()
    )

    by_year_a = {
        snapshot.fiscal_year: snapshot
        for snapshot in snapshots_a
    }
    by_year_b = {
        snapshot.fiscal_year: snapshot
        for snapshot in snapshots_b
    }

    shared_years = set(by_year_a) & set(by_year_b)

    if not shared_years:
        return None

    fiscal_year = max(shared_years)
    snapshot_a = by_year_a[fiscal_year]
    snapshot_b = by_year_b[fiscal_year]

    metrics = []

    for field_name, (display_name, unit) in COMPARISON_FIELDS.items():
        education = METRIC_DEFINITIONS[field_name]

        metrics.append(
            {
                "id": field_name,
                "metric": display_name,
                "definition": education["definition"],
                "formula": education["formula"],
                "why_it_matters": education["why_it_matters"],
                "things_to_consider": education["things_to_consider"],
                "company_a_value": getattr(snapshot_a, field_name),
                "company_b_value": getattr(snapshot_b, field_name),
                "unit": unit,
            }
        )

    return {
        "ticker_a": company_a.ticker,
        "name_a": company_a.name,
        "report_date_a": snapshot_a.report_date,
        "ticker_b": company_b.ticker,
        "name_b": company_b.name,
        "report_date_b": snapshot_b.report_date,
        "fiscal_year": fiscal_year,
        "metrics": metrics,
    }