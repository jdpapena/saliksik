"""Provide company discovery, financial, and comparison endpoints."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.company import CompanyResponse
from app.schemas.company_comparison import CompanyComparisonResponse
from app.schemas.company_search import CompanySearchResult
from app.schemas.financial_snapshot import FinancialSnapshotResponse
from app.services.comparison_service import compare_companies
from app.services.company_data_service import ensure_company_data
from app.services.company_directory_service import (
    search_company_directory,
)
from app.services.company_service import (
    get_company_by_ticker,
    get_company_financials,
)
from app.services.financial_sync_service import (
    sync_annual_financials_from_sec,
)
from app.services.sync_service import sync_company_from_sec


router = APIRouter(
    prefix="/companies",
    tags=["Companies"],
)


# ---------------------------------------------------------------------
# Company discovery
# ---------------------------------------------------------------------


@router.get(
    "/search",
    response_model=list[CompanySearchResult],
)
def search_company_directory_endpoint(
    query: str,
    limit: int = 8,
    database: Session = Depends(get_db),
):
    """Search the complete SEC company directory."""

    if not query.strip():
        return []

    if not 1 <= limit <= 20:
        raise HTTPException(
            status_code=400,
            detail="Limit must be between 1 and 20.",
        )

    return search_company_directory(
        database=database,
        query=query,
        limit=limit,
    )


# ---------------------------------------------------------------------
# Company synchronization
# ---------------------------------------------------------------------


@router.post(
    "/sync/sec/{ticker}",
    response_model=CompanyResponse,
    status_code=201,
)
async def sync_company(
    ticker: str,
    database: Session = Depends(get_db),
):
    """Fetch a US company from SEC EDGAR and save it."""

    company = await sync_company_from_sec(
        database=database,
        ticker=ticker,
    )

    if company is None:
        raise HTTPException(
            status_code=404,
            detail=f"Company '{ticker.upper()}' was not found in SEC EDGAR.",
        )

    return company


@router.post(
    "/{ticker}/financials/sync",
    response_model=list[FinancialSnapshotResponse],
)
async def sync_company_financials(
    ticker: str,
    database: Session = Depends(get_db),
):
    """Fetch and save annual SEC financial facts."""

    normalized_ticker = ticker.strip().upper()

    company = get_company_by_ticker(
        database,
        normalized_ticker,
    )

    if company is None:
        raise HTTPException(
            status_code=404,
            detail=(
                f"Company '{normalized_ticker}' must be synchronized "
                "before its financials."
            ),
        )

    return await sync_annual_financials_from_sec(
        database=database,
        ticker=normalized_ticker,
    )


# ---------------------------------------------------------------------
# Company information
# ---------------------------------------------------------------------


@router.get(
    "/{ticker}/financials",
    response_model=list[FinancialSnapshotResponse],
)
def read_company_financials(
    ticker: str,
    limit: int | None = 5,
    database: Session = Depends(get_db),
):
    """Return stored annual financial facts for one company."""

    if limit is not None and not 1 <= limit <= 30:
        raise HTTPException(
            status_code=400,
            detail="Limit must be between 1 and 30, or omitted.",
        )

    normalized_ticker = ticker.strip().upper()

    company = get_company_by_ticker(
        database,
        normalized_ticker,
    )

    if company is None:
        raise HTTPException(
            status_code=404,
            detail=f"Company '{normalized_ticker}' was not found.",
        )

    return get_company_financials(
        database=database,
        company_id=company.id,
        limit=limit,
    )

@router.get(
    "/{ticker}",
    response_model=CompanyResponse,
)
async def read_company(
    ticker: str,
    database: Session = Depends(get_db),
):
    """Return a company and synchronize missing data."""

    normalized_ticker = ticker.strip().upper()

    company = await ensure_company_data(
        database=database,
        ticker=normalized_ticker,
    )

    if company is None:
        raise HTTPException(
            status_code=404,
            detail=(
                f"Company '{normalized_ticker}' was not found "
                "in SEC EDGAR."
            ),
        )

    return company


# ---------------------------------------------------------------------
# Company comparison
# ---------------------------------------------------------------------


@router.get(
    "/compare/{ticker_a}/{ticker_b}",
    response_model=CompanyComparisonResponse,
)
async def read_company_comparison(
    ticker_a: str,
    ticker_b: str,
    database: Session = Depends(get_db),
):
    """Compare two companies and synchronize missing data."""

    normalized_ticker_a = ticker_a.strip().upper()
    normalized_ticker_b = ticker_b.strip().upper()

    if normalized_ticker_a == normalized_ticker_b:
        raise HTTPException(
            status_code=400,
            detail="Choose two different companies to compare.",
        )

    company_a = await ensure_company_data(
        database=database,
        ticker=normalized_ticker_a,
    )

    company_b = await ensure_company_data(
        database=database,
        ticker=normalized_ticker_b,
    )

    if company_a is None or company_b is None:
        raise HTTPException(
            status_code=404,
            detail="One or both companies were not found in SEC EDGAR.",
        )

    comparison = compare_companies(
        database=database,
        company_a=company_a,
        company_b=company_b,
    )

    if comparison is None:
        raise HTTPException(
            status_code=404,
            detail="No shared fiscal year was found for this comparison.",
        )

    return comparison