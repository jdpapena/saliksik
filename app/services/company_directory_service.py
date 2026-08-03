"""
Synchronize and search the company discovery directory.
"""

from sqlalchemy import case, or_
from sqlalchemy.orm import Session

from app.models.company_directory import CompanyDirectory
from app.providers.sec_company_directory import (
    SecCompanyDirectoryProvider,
)
from app.providers.sec_company_directory_adapter import (
    SecCompanyDirectoryAdapter,
)

async def sync_sec_company_directory(
    database: Session,
) -> int:
    """Download the SEC company directory."""
    provider = SecCompanyDirectoryProvider()
    adapter = SecCompanyDirectoryAdapter()

    raw_data = await provider.get_directory()

    if raw_data is None:
        return 0

    entries = adapter.normalize(raw_data)
    saved_count = 0

    for entry in entries:
        directory_company = (
            database.query(CompanyDirectory)
            .filter(
                CompanyDirectory.ticker == entry.ticker
            )
            .first()
        )

        if directory_company is None:
            directory_company = CompanyDirectory(
                cik=entry.cik,
                ticker=entry.ticker,
                company_name=entry.company_name,
                exchange=entry.exchange,
                country=entry.country,
                source=entry.source,
            )
            database.add(directory_company)
        else:
            directory_company.cik = entry.cik
            directory_company.company_name = entry.company_name
            directory_company.exchange = entry.exchange
            directory_company.country = entry.country
            directory_company.source = entry.source
            directory_company.is_active = True

        saved_count += 1

    database.commit()
    return saved_count

def search_company_directory(
    database: Session,
    query: str,
    limit: int = 8,
) -> list[CompanyDirectory]:
    """Search the full company directory by ticker or name."""
    normalized_query = query.strip()

    if not normalized_query:
        return []

    upper_query = normalized_query.upper()
    contains_pattern = f"%{normalized_query}%"
    starts_pattern = f"{normalized_query}%"

    ranking = case(
        (CompanyDirectory.ticker == upper_query, 0),
        (CompanyDirectory.company_name.ilike(starts_pattern), 1),
        (CompanyDirectory.ticker.ilike(starts_pattern), 2),
        else_=3,
    )

    return (
        database.query(CompanyDirectory)
        .filter(
            CompanyDirectory.is_active.is_(True),
            or_(
                CompanyDirectory.ticker.ilike(
                    contains_pattern
                ),
                CompanyDirectory.company_name.ilike(
                    contains_pattern
                ),
            ),
        )
        .order_by(
            ranking,
            CompanyDirectory.company_name.asc(),
        )
        .limit(limit)
        .all()
    )