from pydantic import BaseModel

class StockSummary(BaseModel):
    ticker: str
    recommendation: str

    strengths: list[str]
    weaknesses: list[str]

    overview: str