from pydantic import BaseModel

class YahooStock(BaseModel):
    ticker: str
    company_name: str

    sector: str | None = None
    industry: str | None = None
    country: str | None = None

    market_cap: int | None = None

    pe_ratio: float | None = None
    beta: float | None = None

    revenue_growth: float | None = None
    earnings_growth: float | None = None

    current_ratio: float | None = None
    debt_to_equity: float | None = None
    return_on_equity: float | None = None
    profit_margins: float | None = None
    free_cash_flow: float | None = None

    recommendation_mean: float | None = None
    recommendation_key: str | None = None
    number_of_analyst_opinions: int | None = None

    