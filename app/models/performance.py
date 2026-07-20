from pydantic import BaseModel

class StockPerformance(BaseModel):
    one_day: float | None
    one_week: float | None
    one_month: float | None
    six_months: float | None
    one_year: float | None
    five_years: float | None