from datetime import datetime, timedelta

import yfinance as yf

from app.models.performance import StockPerformance

# Timeframes
ONE_DAY = 1
ONE_WEEK = 7
ONE_MONTH = 30
SIX_MONTHS = 182
ONE_YEAR = 365
FIVE_YEARS = 365 * 5

def calculate_return_since(history, days: int) -> float | None:
    # Error handling
    if history.empty:
        return None

    target_date = history.index[-1] - timedelta(days = days)
    period_history = history.loc[target_date:]

    if len(period_history) < 2:
        return None

    start = period_history["Close"].iloc[0]
    end = period_history["Close"].iloc[-1]

    return round(((end - start) / start) * 100, 2)

def get_stock_performance(ticker: str) -> StockPerformance:

    history = yf.Ticker(ticker).history(period="5y")
    # Specific timeframes are the most common for evaluating stocks
    return StockPerformance(
        one_day = calculate_return_since(history, ONE_DAY),
        one_week = calculate_return_since(history, ONE_WEEK),
        one_month = calculate_return_since(history, ONE_MONTH),
        six_months = calculate_return_since(history, SIX_MONTHS),
        one_year = calculate_return_since(history, ONE_YEAR),
        five_years = calculate_return_since(history, FIVE_YEARS),
    )