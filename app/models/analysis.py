from pydantic import BaseModel
from app.models.score import Score
from app.models.summary import StockSummary

class StockAnalysis(BaseModel):

    ticker: str
    company_name: str

    sector: str | None = None
    industry: str | None = None
    country: str | None = None
    
    market_cap: int | None = None

    score: Score
    summary: StockSummary