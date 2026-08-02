"""
Stores a company's daily stock price and trading volume.
- This data will later be used for charts and historical comparisons.
"""

from datetime import date
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, Numeric, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.models.company import Company


class HistoricalPrice(Base):
    """Stores one company's market data for one trading day."""

    __tablename__ = "historical_prices"

    # Prevents duplicate price records for the same company and date
    __table_args__ = (
        UniqueConstraint(
            "company_id",
            "price_date",
            name="uq_historical_price_company_date",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    # Links this price record to its company
    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id"),
        index=True,
    )

    # Trading date represented by this row
    price_date: Mapped[date] = mapped_column(Date, index=True)

    # Daily stock prices
    open_price: Mapped[Decimal | None] = mapped_column(Numeric(20, 4))
    high_price: Mapped[Decimal | None] = mapped_column(Numeric(20, 4))
    low_price: Mapped[Decimal | None] = mapped_column(Numeric(20, 4))
    close_price: Mapped[Decimal | None] = mapped_column(Numeric(20, 4))

    # Number of shares traded during the day
    volume: Mapped[int | None]

    # Python-side connection to the related company
    company: Mapped["Company"] = relationship(
        back_populates="historical_prices",
    )