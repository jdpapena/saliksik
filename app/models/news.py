from pydantic import BaseModel

class NewsArticle(BaseModel):
    title: str

    publisher: str | None = None
    published_at: str | None = None

    link: str | None = None
    thumbnail: str | None = None


class StockNews(BaseModel):
    ticker: str
    articles: list[NewsArticle]
