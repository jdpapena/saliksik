from app.models.score import Score, ScoreCategory
from app.services.scoring.utils import calculate_stars

# Financial Health: 30% - biggest indicator on how well the company is doing
# Growth and Valuation: 20% each - big indicator but not as big as the health of finance of a company
# Risk: 20% - another big indicator as a conservative trader myself, it could be doing good now but if it has potential risks you do proceed with caution
# Market Sentiment: 10% - tells a lot on short term movement of the company's value but long-term it becomes more vague and just part of a history

def calculate_overall_score(
    financial_health: ScoreCategory,
    growth: ScoreCategory,
    valuation: ScoreCategory,
    risk: ScoreCategory,
    market_sentiment: ScoreCategory,
) -> Score:
    financial_pct = financial_health.score / financial_health.max_score
    growth_pct = growth.score / growth.max_score
    valuation_pct = valuation.score / valuation.max_score
    risk_pct = risk.score / risk.max_score
    market_sentiment_pct = (
        market_sentiment.score / market_sentiment.max_score
    )

    financial_health_wt = 0.30
    growth_wt = 0.20
    valuation_wt = 0.20
    risk_wt = 0.20
    market_sentiment_wt = 0.10

    overall_score = (
        financial_pct * financial_health_wt
        + growth_pct * growth_wt
        + valuation_pct * valuation_wt
        + risk_pct * risk_wt
        + market_sentiment_pct * market_sentiment_wt
    )

    overall = round(overall_score * 100)

    return Score(
        financial_health = financial_health,
        growth = growth,
        valuation = valuation,
        risk = risk,
        market_sentiment = market_sentiment,
        overall = overall,
        overall_stars = calculate_stars(overall, 100),
        grade = generate_grade(overall),
        assessment = generate_assessment(overall),
        strengths = get_strengths(
            financial_health,
            growth,
            valuation,
            risk,
            market_sentiment,
        ),
        weaknesses = get_weaknesses(
            financial_health,
            growth,
            valuation,
            risk,
            market_sentiment,
        ),
    )


def generate_grade(score: int) -> str:
    grade_a = 85
    grade_b = 75
    grade_c = 65
    grade_d = 50

    if score >= grade_a:
        return "A"

    if score >= grade_b:
        return "B"

    if score >= grade_c:
        return "C"

    if score >= grade_d:
        return "D"

    return "F"


def generate_assessment(overall_score: int) -> str:
    if overall_score >= 90:
        return "Excellent"

    if overall_score >= 80:
        return "Strong"

    if overall_score >= 70:
        return "Good"

    if overall_score >= 60:
        return "Fair"

    if overall_score >= 40:
        return "Weak"

    return "High Risk"


def get_strengths(
    financial_health: ScoreCategory,
    growth: ScoreCategory,
    valuation: ScoreCategory,
    risk: ScoreCategory,
    market_sentiment: ScoreCategory,
) -> list[str]:
    strengths: list[str] = []

    if financial_health.stars >= 4:
        strengths.append("Strong financial health")

    if growth.stars >= 4:
        strengths.append("Strong business growth")

    if valuation.stars >= 4:
        strengths.append("Attractive valuation")

    if risk.stars >= 4:
        strengths.append("Low market risk")

    if market_sentiment.stars >= 4:
        strengths.append("Positive analyst sentiment")

    return strengths


def get_weaknesses(
    financial_health: ScoreCategory,
    growth: ScoreCategory,
    valuation: ScoreCategory,
    risk: ScoreCategory,
    market_sentiment: ScoreCategory,
) -> list[str]:
    weaknesses: list[str] = []

    if financial_health.stars <= 2:
        weaknesses.append("Weak financial health")

    if growth.stars <= 2:
        weaknesses.append("Slow business growth")

    if valuation.stars <= 2:
        weaknesses.append("Premium valuation")

    if risk.stars <= 2:
        weaknesses.append("High market risk")

    if market_sentiment.stars <= 2:
        weaknesses.append("Negative analyst sentiment")

    return weaknesses