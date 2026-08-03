from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException

from app.database.dependencies import get_db
from app.schemas.company import CompanyResponse
from app.schemas.financial_snapshot import FinancialSnapshotResponse
from app.schemas.company_comparison import CompanyComparisonResponse
from app.services.comparison_service import compare_companies
from app.services.company_service import (
    get_all_companies,
    get_company_by_ticker,
    get_company_financials
)
from app.services.company_data_service import ensure_company_data
from app.services.sync_service import sync_company_from_sec
from app.services.financial_sync_service import (
    sync_annual_financials_from_sec,
)

router = APIRouter(
    prefix="/companies",
    tags=["Companies"],
)

@router.post(
    "/{ticker}/financials/sync",
    response_model=list[FinancialSnapshotResponse],
)
async def sync_company_financials(
    ticker: str,
    database: Session = Depends(get_db),
):
    """Fetch and save annual SEC financial facts."""
    company = get_company_by_ticker(
        database,
        ticker.upper(),
    )

    if company is None:
        raise HTTPException(
            status_code=404,
            detail="Synchronize the company before its financials.",
        )

    return await sync_annual_financials_from_sec(
        database=database,
        ticker=ticker,
    )

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
            detail="Company not found in SEC EDGAR.",
        )

    return company

@router.get(
    "/{ticker}/financials",
    response_model=list[FinancialSnapshotResponse],
)
def read_company_financials(
    ticker: str,
    limit: int | None = 5,
    database: Session = Depends(get_db),
):
    """Return the latest stored annual financial facts."""
    if limit is not None and not 1 <= limit <= 30:
        raise HTTPException(
            status_code=400,
            detail="Limit must be between 1 and 30, or omitted.",
        )

    company = get_company_by_ticker(
        database,
        ticker.upper(),
    )

    if company is None:
        raise HTTPException(
            status_code=404,
            detail="Company not found.",
        )

    return get_company_financials(
        database=database,
        company_id=company.id,
        limit=limit,
    )

@router.get(
    "/compare/{ticker_a}/{ticker_b}",
    response_model=CompanyComparisonResponse,
)
async def read_company_comparison(
    ticker_a: str,
    ticker_b: str,
    database: Session = Depends(get_db),
):
    """Compare two companies and synchronize missing data automatically."""
    company_a = await ensure_company_data(
        database=database,
        ticker=ticker_a,
    )

    company_b = await ensure_company_data(
        database=database,
        ticker=ticker_b,
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
            detail="No shared financial year was found.",
        )

    return comparison

@router.get(
    "/{ticker}",
    response_model=CompanyResponse,
)

def read_company(
    ticker: str,
    database: Session = Depends(get_db),
):
    """Return one company using its ticker."""
    company = get_company_by_ticker(
        database,
        ticker.upper(),
    )

    if company is None:
        raise HTTPException(
            status_code=404,
            detail="Company not found.",
        )
    
    return company