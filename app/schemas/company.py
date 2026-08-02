from pydantic import BaseModel, ConfigDict

class CompanyResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    ticker: str
    name: str
    exchange: str
    country: str
    sector: str
    industry: str
    description: str
    website: str
    market_cap: int
    currency: str
    employees: int