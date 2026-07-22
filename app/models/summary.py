from pydantic import BaseModel

class StockSummary(BaseModel):
    ticker: str
    assessment: str
    strengths: list[str]
    weaknesses: list[str]
    overview: str