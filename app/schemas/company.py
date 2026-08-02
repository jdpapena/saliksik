from pydantic import BaseModel, ConfigDict

class CompanyResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    ticker: str
    name: str
    exchange: str
    asset_type: str

    # The data may be unavailable on some APIs
    country: str | None = None
    sector: str | None = None
    industry: str | None = None
    description: str | None = None
    website: str | None = None
    market_cap: int | None = None
    currency: str | None = None
    employees: int | None = None