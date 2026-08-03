"""
Schemas for company search results.
"""

from pydantic import BaseModel

class CompanySearchResult(BaseModel):
    ticker: str
    name: str
    exchange: str