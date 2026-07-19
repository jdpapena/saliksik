from app.models.score import ScoreCategory
from app.services.scoring.utils import calculate_stars

def calculate_valuation(pe_ratio: float | None) -> ScoreCategory:
    score = 0

    # Missing data
    if pe_ratio is None:
        return ScoreCategory(
            score=0,
            max_score=20,
            stars=1,
            explanation="P/E ratio is unavailable, so valuation could not be assessed.",
        )

    # Invalid value
    if pe_ratio < 0:
        raise ValueError("PE Ratio cannot be negative.")

    if pe_ratio < 10:
        score = 15
    elif pe_ratio <= 25:
        score = 20
    elif pe_ratio <= 35:
        score = 15
    elif pe_ratio <= 50:
        score = 8
    else:
        score = 3

    stars = calculate_stars(score, 20)
    explanation = generate_valuation_explanation(score)

    return ScoreCategory(
        score = score,
        max_score = 20,
        stars = stars,
        explanation = explanation,
    )

def generate_valuation_explanation(score: int) -> str:
    if score >= 18:
        return (
            "The stock appears fairly valued with a reasonable price-to-earnings ratio."
        )
    elif score >= 12:
        return (
            "The valuation is acceptable, though investors should compare it with industry peers."
        )
    elif score >= 6:
        return (
            "The stock may be overvalued. Investors should proceed carefully."
        )
    else:
        return (
            "The stock appears significantly overvalued based on its P/E ratio."
        )