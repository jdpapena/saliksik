from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException

from app.database.dependencies import get_db
from app.schemas.company import CompanyResponse
from app.services.company_service import (
    get_all_companies,
    get_company_by_ticker,
)
from app.services.sync_service import sync_company_from_sec

router = APIRouter(
    prefix="/companies",
    tags=["Companies"],
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