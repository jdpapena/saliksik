from app.models.analysis import StockAnalysis
from app.models.score import ScoreCategory

from app.services.yahoo_finance_service import get_stock_info
from app.services.scoring.financial_health import calculate_financial_health
from app.services.scoring.growth import calculate_growth
from app.services.scoring.valuation import calculate_valuation
from app.services.scoring.risk import calculate_risk
from app.services.scoring.overall import calculate_overall_score
from app.services.scoring.market_sentiment import calculate_market_sentiment
from app.services.summary_service import generate_summary

def analyze_stock(ticker: str) -> StockAnalysis:

    stock = get_stock_info(ticker)

    financial_health = calculate_financial_health(
        debt_to_equity = stock.debt_to_equity,
        current_ratio = stock.current_ratio,
        free_cash_flow = stock.free_cash_flow,
    )

    growth = calculate_growth(
        revenue_growth = stock.revenue_growth,
        earnings_growth = stock.earnings_growth,
    )

    valuation = calculate_valuation(
        pe_ratio = stock.pe_ratio,
    )

    risk = calculate_risk(
        beta = stock.beta,
    )

    market_sentiment = calculate_market_sentiment(
        recommendation_mean=stock.recommendation_mean,
        recommendation_key=stock.recommendation_key,
        analyst_count=stock.number_of_analyst_opinions,
    )

    overall = calculate_overall_score(
        financial_health,
        growth,
        valuation,
        risk,
        market_sentiment,
    )

    summary = generate_summary(
        company_name = stock.company_name,
        score = overall,
    )

    return StockAnalysis(
        ticker = stock.ticker,
        company_name = stock.company_name,
        sector = stock.sector,
        market_cap = stock.market_cap,
        score = overall,
        summary = summary,
    )
