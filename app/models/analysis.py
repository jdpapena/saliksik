from pydantic import BaseModel
from app.models.score import Score

class StockAnalysis(BaseModel):

    ticker: str
    company_name: str
    sector: str | None = None
    market_cap: int | None = None

    score: Score