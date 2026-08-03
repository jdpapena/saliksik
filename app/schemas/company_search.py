"""
Schemas for company directory search results.
"""

from pydantic import BaseModel

class CompanySearchResult(BaseModel):
    ticker: str
    company_name: str
    exchange: str | None
    source: str