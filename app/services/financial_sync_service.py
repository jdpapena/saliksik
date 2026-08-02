"""
Save normalized annual financial facts to the database.
"""

from sqlalchemy.orm import Session

from app.models.company import Company
from app.models.financial_snapshot import FinancialSnapshot
from app.providers.sec_financial_adapter import SecFinancialAdapter
from app.providers.sec_financials import SecFinancialsProvider

async def sync_annual_financials_from_sec(
    database: Session,
    ticker: str,
) -> list[FinancialSnapshot]:
    """Fetch, normalize, and save annual SEC financial facts."""

    normalized_ticker = ticker.upper()

    company = (
        database.query(Company)
        .filter(Company.ticker == normalized_ticker)
        .first()
    )

    if company is None:
        raise ValueError(
            "Company must be synchronized before financials."
        )

    provider = SecFinancialsProvider()
    adapter = SecFinancialAdapter()

    raw_data = await provider.get_company_facts(
        normalized_ticker
    )

    if raw_data is None:
        return []

    normalized_snapshots = adapter.normalize(raw_data)
    saved_snapshots: list[FinancialSnapshot] = []

    for normalized in normalized_snapshots:
        snapshot = (
            database.query(FinancialSnapshot)
            .filter(
                FinancialSnapshot.company_id == company.id,
                FinancialSnapshot.fiscal_year
                == normalized.fiscal_year,
                FinancialSnapshot.fiscal_period
                == normalized.fiscal_period,
            )
            .first()
        )

        if snapshot is None:
            snapshot = FinancialSnapshot(
                company_id=company.id,
                fiscal_year=normalized.fiscal_year,
                fiscal_period=normalized.fiscal_period,
                report_date=normalized.report_date,
            )
            database.add(snapshot)

        for field_name, value in vars(normalized).items():
            setattr(snapshot, field_name, value)

        saved_snapshots.append(snapshot)

    database.commit()

    for snapshot in saved_snapshots:
        database.refresh(snapshot)

    return saved_snapshots