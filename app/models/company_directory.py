"""
Lightweight company records used for search and discovery.

A directory entry helps users find a company before its complete
profile and financial statements have been synchronized.
"""

from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base

class CompanyDirectory(Base):
    """Represents one searchable company-directory entry."""
    __tablename__ = "company_directory"

    id: Mapped[int] = mapped_column(primary_key=True)

    # Provider-specific company identifier, such as an SEC CIK.
    cik: Mapped[int] = mapped_column(
        Integer,
        index=True,
    )

    ticker: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        index=True,
    )

    company_name: Mapped[str] = mapped_column(
        String(255),
        index=True,
    )

    # These can be enriched later from other providers.
    exchange: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    country: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    sector: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    industry: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    source: Mapped[str] = mapped_column(
        String(50),
        default="SEC",
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    last_updated: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )