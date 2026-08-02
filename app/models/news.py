"""
API response models for stock news.
"""

from pydantic import BaseModel


class NewsArticle(BaseModel):
    """One news article returned by the stock news endpoint."""

    title: str
    publisher: str | None = None
    published_at: str | None = None
    link: str | None = None
    thumbnail: str | None = None


class StockNews(BaseModel):
    """Collection of news articles for one ticker."""

    ticker: str
    articles: list[NewsArticle]