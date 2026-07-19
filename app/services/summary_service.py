from app.models.score import Score

def generate_summary(company_name: str, score: Score,) -> str:

    summary = []

    summary.append(
        f"{company_name} received an overall {score.recommendation} recommendation."
    )

    if score.financial_health.stars >= 4:
        summary.append(
            "The company demonstrates strong financial health."
        )
    elif score.financial_health.stars <= 2:
        summary.append(
            "Its financial health shows some areas of concern."
        )

    if score.growth.stars >= 4:
        summary.append(
            "Revenue and earnings growth are strong."
        )
    elif score.growth.stars <= 2:
        summary.append(
            "Business growth has been relatively weak."
        )

    if score.valuation.stars <= 2:
        summary.append(
            "The stock appears to trade at a relatively expensive valuation."
        )
    elif score.valuation.stars >= 4:
        summary.append(
            "The stock appears attractively valued."
        )

    if score.risk.stars <= 2:
        summary.append(
            "Investors should be aware of elevated volatility."
        )

    if score.market_sentiment.stars >= 4:
        summary.append(
            "Analysts generally maintain a positive outlook."
        )

    return " ".join(summary)