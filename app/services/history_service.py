import yfinance as yf

from app.models.history import HistoricalPrice

def get_stock_history(ticker: str, period: str = "1y",) -> list[HistoricalPrice]:

    stock = yf.Ticker(ticker)
    history = stock.history(period=period)

    prices = []

    for date, row in history.iterrows():
        prices.append(
            HistoricalPrice(
                date = date.strftime("%Y-%m-%d"),
                open = float(row["Open"]),
                high = float(row["High"]),
                low = float(row["Low"]),
                close = float(row["Close"]),
                volume = int(row["Volume"]),
            )
        )

    return prices