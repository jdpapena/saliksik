"""
Database model for company news articles.
"""

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.models.company import Company


class NewsRecord(Base):
    """Stores one news article associated with a company."""

    __tablename__ = "news"

    id: Mapped[int] = mapped_column(primary_key=True)

    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id"),
        index=True,
    )

    title: Mapped[str] = mapped_column(String(300))
    source: Mapped[str] = mapped_column(String(100))
    url: Mapped[str] = mapped_column(String(500))
    published_at: Mapped[datetime] = mapped_column(DateTime)
    summary: Mapped[str | None] = mapped_column(Text)

    company: Mapped["Company"] = relationship(
        back_populates="news_articles",
    )