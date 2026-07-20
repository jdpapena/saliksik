from app.models.summary import StockSummary
from app.models.score import Score

def generate_summary(
    ticker: str,
    company_name: str,
    score: Score,
) -> StockSummary:

    strengths = []
    weaknesses = []
    overview = [f"{company_name} earns a {score.recommendation} recommendation."]

    # Financial Health
    if score.financial_health.stars >= 4:
        strengths.append("Strong financial health")
        overview.append("The company has a strong financial foundation.")
    elif score.financial_health.stars <= 2:
        weaknesses.append("Weak financial health")
        overview.append("The company's financial position shows some areas of concern.")

    # Growth
    if score.growth.stars >= 4:
        strengths.append("Steady business growth")
        overview.append("The business continues to grow at a healthy pace.")
    elif score.growth.stars <= 2:
        weaknesses.append("Slow business growth")
        overview.append("Recent business growth has been slower than expected.")

    # Valuation
    if score.valuation.stars >= 4:
        strengths.append("Attractive valuation")
        overview.append("The current share price appears attractive relative to the company's fundamentals.")
    elif score.valuation.stars <= 2:
        weaknesses.append("Premium stock price")
        overview.append("Investors are currently paying a premium for its shares.")

    # Risk
    if score.risk.stars >= 4:
        strengths.append("Low investment risk")
        overview.append("The stock has shown relatively stable price movements.")
    elif score.risk.stars <= 2:
        weaknesses.append("High price volatility")
        overview.append("The stock may experience larger price swings than average.")

    # Market Sentiment
    if score.market_sentiment.stars >= 4:
        strengths.append("Positive analyst sentiment")
        overview.append("Most analysts remain optimistic about the company's future.")
    elif score.market_sentiment.stars <= 2:
        weaknesses.append("Negative analyst sentiment")
        overview.append("Analyst sentiment has become more cautious.")

    if score.recommendation == "STRONG BUY":
        overview.append("Overall, the company stands out as one of the strongest investment opportunities based on its current fundamentals.")

    elif score.recommendation == "BUY":
        overview.append("Overall, the company appears well-positioned for long-term investors.")

    elif score.recommendation == "HOLD":
        overview.append("Overall, the company appears stable, but investors may prefer waiting for a more attractive entry price.")

    elif score.recommendation == "WATCH":
        overview.append("Overall, investors should monitor future developments before making an investment decision.")

    else:
        overview.append("Overall, investors should approach this stock cautiously until its fundamentals improve.")

    return StockSummary(
        ticker = ticker,
        recommendation = score.recommendation,
        strengths = strengths,
        weaknesses = weaknesses,
        overview = " ".join(overview),
    )