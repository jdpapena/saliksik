"""
Handles database operations related to companies.
"""

from sqlalchemy.orm import Session

from app.models.company import Company


def create_company(
    database: Session,
    *,
    ticker: str,
    name: str,
    exchange: str,
    country: str,
    sector: str,
    industry: str,
    description: str,
    website: str,
    market_cap: int,
    currency: str,
    employees: int,
) -> Company:
    """Create and save a company in the database."""

    company = Company(
        ticker=ticker,
        name=name,
        exchange=exchange,
        country=country,
        sector=sector,
        industry=industry,
        description=description,
        website=website,
        market_cap=market_cap,
        currency=currency,
        employees=employees,
    )

    database.add(company)
    database.commit()
    database.refresh(company)

    return company

def get_company_by_ticker(
    database: Session,
    ticker: str,
) -> Company | None:

    return (
        database.query(Company)
        .filter(Company.ticker == ticker)
        .first()
    )

def get_all_companies(
    database: Session,
) -> list[Company]:

    return (
        database.query(Company)
        .order_by(Company.ticker)
        .all()
    )

def update_company(
    database: Session,
    company: Company,
    **updates,
) -> Company:

    for field, value in updates.items():
        if hasattr(company, field):
            setattr(company, field, value)

    database.commit()
    database.refresh(company)

    return company

def delete_company(
    database: Session,
    company: Company,
) -> None:

    database.delete(company)
    database.commit()