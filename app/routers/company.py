from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException

from app.database.dependencies import get_db
from app.schemas.company import CompanyResponse
from app.services.company_service import (
    get_all_companies,
    get_company_by_ticker,
)

router = APIRouter(
    prefix="/companies",
    tags=["Companies"],
)

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