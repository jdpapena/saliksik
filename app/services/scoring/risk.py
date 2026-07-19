from app.models.score import ScoreCategory
from app.services.scoring.utils import calculate_stars

def calculate_risk(beta: float | None) -> ScoreCategory:
    score = 0

    # Missing data
    if beta is None:
        return ScoreCategory(
            score = 0,
            max_score = 10,
            stars = 1,
            explanation = "Beta is unavailable, so risk could not be assessed.",
        )

    # Invalid value
    if beta < 0:
        raise ValueError("Beta cannot be negative.")

    if beta > 10:
        raise ValueError(
            "Beta value is absurdly high. Please check the source."
        )

    if beta <= 1.0:
        score = 10
    elif beta <= 1.5:
        score = 7
    else:
        score = 4

    stars = calculate_stars(score, 10)
    explanation = generate_risk_explanation(score)

    return ScoreCategory(
        score = score,
        max_score = 10,
        stars = stars,
        explanation = explanation,
    )

def generate_risk_explanation(score: int) -> str:
    if score >= 10:
        return (
            "Low volatility. The stock is relatively stable compared to the overall market."
        )
    elif score >= 7:
        return (
            "Moderate volatility. Price fluctuations are noticeable but generally manageable."
        )
    else:
        return (
            "High volatility. This stock carries higher market risk and may not be suitable for conservative investors."
        )