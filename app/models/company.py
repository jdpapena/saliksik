"""
Stores basic information about every company that SALIKSIK supports.

Examples:
    - Apple (AAPL)
    - NVIDIA (NVDA)
    - AREIT
    - MBT

- This table stores company information only. Financial data, prices, dividends, and news will be stored
in their own tables.
"""

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.financial_snapshot import FinancialSnapshot
    from app.models.historical_price import HistoricalPrice
    from app.models.dividend import Dividend
    from app.models.news_record import NewsRecord
    from app.models.saved_company import SavedCompany

class Company(Base):
    """Represents a publicly listed company."""

    __tablename__ = "companies"

    # Primary key used internally by the database
    id: Mapped[int] = mapped_column(primary_key=True)

    # Stock ticker (e.g. AAPL, NVDA, AREIT)
    ticker: Mapped[str] = mapped_column(String(10), unique=True, index=True)

    # Full company name
    name: Mapped[str] = mapped_column(String(255))

    # Exchange where the company is listed
    exchange: Mapped[str] = mapped_column(String(20))

    # Country of the stock market
    country: Mapped[str] = mapped_column(String(50))

    # Business classification
    sector: Mapped[str] = mapped_column(String(100))
    industry: Mapped[str] = mapped_column(String(100))

    # Short company description
    description: Mapped[str] = mapped_column(String(2000))

    # Official company website
    website: Mapped[str] = mapped_column(String(255))

    # Company size
    market_cap: Mapped[int] = mapped_column(Integer)

    # Trading currency (USD, PHP, etc.)
    currency: Mapped[str] = mapped_column(String(10))

    # Number of employees
    employees: Mapped[int] = mapped_column(Integer)

    # Historical financial reports
    financial_snapshots: Mapped[list["FinancialSnapshot"]] = relationship(
        back_populates="company",
        cascade="all, delete-orphan",
    )

    # Daily stock-price records 
    historical_prices: Mapped[list["HistoricalPrice"]] = relationship(
        back_populates="company",
        cascade="all, delete-orphan",
    )

    # Dividend history
    dividends: Mapped[list["Dividend"]] = relationship(
        back_populates="company",
        cascade="all, delete-orphan",
    )

    # News articles mentioning the company
    news_articles: Mapped[list["NewsRecord"]] = relationship(
        back_populates="company",
        cascade="all, delete-orphan",
    )

    # Users who bookmarked the company
    saved_by_users: Mapped[list["SavedCompany"]] = relationship(
        back_populates="company",
        cascade="all, delete-orphan",
    )