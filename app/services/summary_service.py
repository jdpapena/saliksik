from app.models.summary import StockSummary
from app.models.score import Score

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


def generate_summary(
    ticker: str,
    company_name: str,
    score: Score,
) -> StockSummary:

    strengths = []
    weaknesses = []

    assessment = generate_assessment(score.overall)

    overview = [
        f"{company_name} demonstrates {assessment.lower()} overall fundamentals."
    ]

    # Financial Health
    if score.financial_health.stars >= 4:
        strengths.append("Strong financial health")
        overview.append(
            "The company has a strong financial foundation."
        )
    elif score.financial_health.stars <= 2:
        weaknesses.append("Weak financial health")
        overview.append(
            "The company's financial position shows some areas of concern."
        )

    # Growth
    if score.growth.stars >= 4:
        strengths.append("Steady business growth")
        overview.append(
            "The business continues to grow at a healthy pace."
        )
    elif score.growth.stars <= 2:
        weaknesses.append("Slow business growth")
        overview.append(
            "Recent business growth has been slower than expected."
        )

    # Valuation
    if score.valuation.stars >= 4:
        strengths.append("Attractive valuation")
        overview.append(
            "The current share price appears attractive relative to the company's fundamentals."
        )
    elif score.valuation.stars <= 2:
        weaknesses.append("Premium stock price")
        overview.append(
            "Investors are currently paying a premium for its shares."
        )

    # Risk
    if score.risk.stars >= 4:
        strengths.append("Relatively stable price behavior")
        overview.append(
            "The stock has shown relatively stable price movements."
        )
    elif score.risk.stars <= 2:
        weaknesses.append("High price volatility")
        overview.append(
            "The stock may experience larger price swings than average."
        )

    # Market Sentiment
    if score.market_sentiment.stars >= 4:
        strengths.append("Positive analyst sentiment")
        overview.append(
            "Analyst sentiment toward the company is generally positive."
        )
    elif score.market_sentiment.stars <= 2:
        weaknesses.append("Cautious analyst sentiment")
        overview.append(
            "Analyst sentiment toward the company is currently more cautious."
        )

    # Overall Assessment
    if assessment == "Excellent":
        overview.append(
            "Overall, the company demonstrates outstanding financial characteristics "
            "and may be worthy of further research by long-term investors."
        )

    elif assessment == "Strong":
        overview.append(
            "Overall, the company demonstrates solid financial characteristics "
            "and may be worthy of further research."
        )

    elif assessment == "Good":
        overview.append(
            "Overall, the company shows generally positive fundamentals, "
            "although some areas deserve closer attention."
        )

    elif assessment == "Fair":
        overview.append(
            "Overall, the company has mixed fundamentals and requires closer evaluation."
        )

    elif assessment == "Weak":
        overview.append(
            "Overall, the company has several fundamental concerns "
            "that should be carefully reviewed."
        )

    else:
        overview.append(
            "Overall, the company currently exhibits significant financial "
            "or market-related risks that require careful evaluation."
        )

    return StockSummary(
        ticker = ticker,
        assessment = assessment,
        strengths = strengths,
        weaknesses = weaknesses,
        overview = " ".join(overview),
    )