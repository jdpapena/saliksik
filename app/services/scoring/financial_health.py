from app.models.score import ScoreCategory
from app.services.scoring.utils import calculate_stars

def calculate_financial_health(debt_to_equity: float | None, current_ratio: float | None, free_cash_flow: float | None,) -> ScoreCategory:
    
    score = 0

    if debt_to_equity is not None:
        if debt_to_equity < 1.0:
            score += 10
        elif debt_to_equity < 2.0:
            score += 6
        else:
            score += 2

    if current_ratio is not None:
        if current_ratio >= 2.0:
            score += 10
        elif current_ratio >= 1.0:
            score += 6
        else:
            score += 2

    if free_cash_flow is not None:
        if free_cash_flow > 0:
            score += 10

    stars = calculate_stars(score, 30)

    explanation = generate_financial_health_explanation(score)

    return ScoreCategory(
        score=score,
        max_score=30,
        stars=stars,
        explanation=explanation,
    )  

def generate_financial_health_explanation(score: int) -> str:
    if score >= 27:
        return (
            "Excellent financial health with low debt, strong liquidity, and positive cash flow."
        )
    elif score >= 20:
        return (
            "Good financial health, though some financial metrics could improve."
        )
    elif score >= 12:
        return (
            "Average financial health. Investors should review the company's financial statements carefully."
        )
    else:
        return (
            "Weak financial health due to higher financial risk or weaker cash generation."
        )
