from pydantic import BaseModel

class ScoreCategory(BaseModel):
    score: int
    max_score: int
    stars: int
    explanation: str

class Score(BaseModel):
    financial_health: ScoreCategory
    growth: ScoreCategory
    valuation: ScoreCategory
    market_sentiment: ScoreCategory
    risk: ScoreCategory

    overall: int
    overall_stars: int
    grade: str
    assessment: str

    strengths: list[str]
    weaknesses: list[str]