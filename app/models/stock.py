from pydantic import BaseModel

class Stock(BaseModel):
    symbol: str
    company: str
    market: str
    sector: str