"""
Stores every dividend declared by a company.
"""

# Standard library imports
from datetime import date
from decimal import Decimal
from typing import TYPE_CHECKING

# Third-party imports
from sqlalchemy import Date, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Local imports
from app.database.base import Base

# Imports only used for type hints
if TYPE_CHECKING:
    from app.models.company import Company


class Dividend(Base):
    """Represents one dividend payment."""

    __tablename__ = "dividends"

    # Primary key
    id: Mapped[int] = mapped_column(primary_key=True)

    # Foreign key
    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id"),
        index=True,
    )

    # Dividend timeline
    declaration_date: Mapped[date | None] = mapped_column(Date)
    ex_dividend_date: Mapped[date] = mapped_column(Date, index=True)
    record_date: Mapped[date | None] = mapped_column(Date)
    payment_date: Mapped[date | None] = mapped_column(Date)

    # Cash dividend per share
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 4))

    # Currency (USD, PHP, etc.)
    currency: Mapped[str]

    # Relationship
    company: Mapped["Company"] = relationship(
        back_populates="dividends",
    )

    # Closing price before the stock traded ex-dividend
    previous_close_price: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 4)
    )

    # Historical dividend yield
    historical_yield: Mapped[Decimal | None] = mapped_column(
        Numeric(8, 4)
    )