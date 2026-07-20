from pydantic import BaseModel

class CompanyProfile(BaseModel):
    ticker: str
    company_name: str

    description: str | None = None

    sector: str | None = None
    industry: str | None = None

    ceo: str | None = None

    employees: int | None = None

    country: str | None = None
    city: str | None = None

    website: str | None = None

    market_cap: int | None = None
    market_cap_category: str | None = None