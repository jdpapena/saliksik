from app.models.score import ScoreCategory
from app.services.scoring.utils import calculate_stars

def calculate_growth(revenue_growth: float | None, earnings_growth: float | None,) -> ScoreCategory:
    score = 0

    if revenue_growth is not None:
        if revenue_growth >= 15:
            score += 13
        elif revenue_growth >= 5:
            score += 8
        elif revenue_growth >= 0:
            score += 3

    if earnings_growth is not None:
        if earnings_growth >= 15:
            score += 12
        elif earnings_growth >= 5:
            score += 8
        elif earnings_growth >= 0:
            score += 3

    stars = calculate_stars(score, 25)
    explanation = generate_growth_explanation(score)

    return ScoreCategory(
        score = score,
        max_score = 25,
        stars = stars,
        explanation = explanation,
    )

def generate_growth_explanation(score: int) -> str:
    if score >= 22:
        return (
            "Excellent growth with strong revenue and earnings expansion."
        )
    elif score >= 15:
        return (
            "Healthy growth with consistent business expansion."
        )
    elif score >= 8:
        return (
            "Moderate growth. The company is growing, but at a slower pace."
        )
    else:
        return (
            "Weak growth. Revenue and earnings are showing limited improvement."
        )
