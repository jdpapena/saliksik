"""
Ensure required company data exists before it is used.
"""

from datetime import date

from sqlalchemy.orm import Session

from app.models.company import Company
from app.models.financial_snapshot import FinancialSnapshot
from app.services.financial_sync_service import (
    sync_annual_financials_from_sec,
)
from app.services.sync_service import sync_company_from_sec


async def ensure_company_data(database: Session, ticker: str,) -> Company | None:

    """Fetch and cache company data when it is missing or outdated."""
    normalized_ticker = ticker.strip().upper()

    company = (
        database.query(Company)
        .filter(Company.ticker == normalized_ticker)
        .first()
    )

    if company is None:
        company = await sync_company_from_sec(
            database=database,
            ticker=normalized_ticker,
        )

    if company is None:
        return None

    latest_snapshot = (
        database.query(FinancialSnapshot)
        .filter(FinancialSnapshot.company_id == company.id)
        .order_by(FinancialSnapshot.fiscal_year.desc())
        .first()
    )

    current_year = date.today().year

    # Sync if no financial data exists or the newest stored
    # fiscal year is more than one year behind.
    financials_are_missing = latest_snapshot is None
    financials_may_be_stale = (
        latest_snapshot is not None
        and latest_snapshot.fiscal_year < current_year - 1
    )

    if financials_are_missing or financials_may_be_stale:
        await sync_annual_financials_from_sec(
            database=database,
            ticker=normalized_ticker,
        )

    return company