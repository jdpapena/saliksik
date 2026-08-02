"""
Retrieves official company information from SEC EDGAR 
and saves it to the SALIKSIK database.
"""

from sqlalchemy.orm import Session

from app.models.company import Company
from app.providers.sec_edgar import SecEdgarProvider

async def sync_company_from_sec(
    database: Session,
    ticker: str,
) -> Company | None:
    """Create or update one US company using SEC data."""
    normalized_ticker = ticker.upper()
    provider = SecEdgarProvider()

    company_data = await provider.get_company_submissions(
        normalized_ticker
    )

    if company_data is None:
        return None

    # Look for an existing company before creating a new row.
    company = (
        database.query(Company)
        .filter(Company.ticker == normalized_ticker)
        .first()
    )

    exchange = (
        company_data["exchanges"][0]
        if company_data.get("exchanges")
        else "Unknown"
    )

    if company is None:
        company = Company(
            ticker=normalized_ticker,
            name=company_data["name"],
            exchange=exchange,
            asset_type="stock",
            country="United States",
            industry=company_data.get("sicDescription"),
            currency="USD",
        )

        database.add(company)

    else:
        company.name = company_data["name"]
        company.exchange = exchange
        company.industry = company_data.get("sicDescription")

    database.commit()
    database.refresh(company)

    return company