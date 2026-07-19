from app.models.score import ScoreCategory
from app.services.scoring.utils import calculate_stars

def calculate_market_sentiment(recommendation_mean: float | None, recommendation_key: str | None, analyst_count: int | None,) -> ScoreCategory:
    score = 5

    if recommendation_mean is not None:
        if recommendation_mean <= 1.5:
            score = 10
        elif recommendation_mean <= 2.5:
            score = 8
        elif recommendation_mean <= 3.5:
            score = 5
        elif recommendation_mean <= 4.5:
            score = 2
        else:
            score = 0

    elif recommendation_key is not None:
        recommendation = recommendation_key.lower()

        if recommendation == "strong_buy":
            score = 10
        elif recommendation == "buy":
            score = 8
        elif recommendation == "hold":
            score = 5
        elif recommendation in ("underperform", "under_perform"):
            score = 2
        elif recommendation in ("sell", "strong_sell"):
            score = 0

    # Analysts
    if analyst_count is not None:

        if analyst_count >= 30:
            score += 1

        elif analyst_count <= 5:
            score -= 1
    
    score = max(0, min(score, 10))
    
    stars = calculate_stars(score, 10)
    explanation = generate_market_sentiment_explanation(score)

    return ScoreCategory(
        score = score,
        max_score = 10,
        stars = stars,
        explanation = explanation,
    )

def generate_market_sentiment_explanation(score: int) -> str:

    if score >= 9:
        return (
            "Analysts are highly bullish and expect strong future performance."
        )
    elif score >= 7:
        return (
            "Analysts generally have a positive outlook on the company."
        )
    elif score >= 5:
        return (
            "Analysts have a neutral outlook. There is no strong consensus."
        )
    elif score >= 2:
        return (
            "Analysts are becoming cautious due to potential risks."
        )
    return (
        "Analysts have a bearish outlook and expect weaker future performance."
    )