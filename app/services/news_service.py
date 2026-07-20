import yfinance as yf

from app.models.news import NewsArticle, StockNews

def get_stock_news(ticker: str) -> StockNews:

    stock = yf.Ticker(ticker)

    articles = []

    for article in stock.news:

        content = article.get("content", {})
        provider = content.get("provider", {})
        thumbnail = content.get("thumbnail", {})
        canonical = content.get("canonicalUrl", {})
        click = content.get("clickThroughUrl", {})

        articles.append(
            NewsArticle(
                title = content.get("title"),
                publisher = provider.get("displayName"),
                published_at = content.get("pubDate"),
                link = (click.get("url") or canonical.get("url")),
                thumbnail = thumbnail.get("originalUrl"),
            )
        )

    return StockNews(
        ticker = ticker.upper(),
        articles = articles,
    )
