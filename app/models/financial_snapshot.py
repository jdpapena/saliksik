"""

Purpose:
    Stores a company's financial data for a specific reporting date.

Examples:
    - Annual report for 2025
    - Quarterly report for Q2 2026

"""

from datetime import date
from decimal import Decimal

from sqlalchemy import Date, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class FinancialSnapshot(Base):
    """Stores financial facts reported by a company."""

    __tablename__ = "financial_snapshots"

    # Unique database identifier for this financial record
    id: Mapped[int] = mapped_column(primary_key=True)

    # Connects snapshot to one company
    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id"),
        index=True,
    )

    # Date covered by the financial report
    report_date: Mapped[date] = mapped_column(Date, index=True)

    # Main financial values
    revenue: Mapped[Decimal | None] = mapped_column(Numeric(20, 2))
    net_income: Mapped[Decimal | None] = mapped_column(Numeric(20, 2))
    free_cash_flow: Mapped[Decimal | None] = mapped_column(Numeric(20, 2))
    earnings_per_share: Mapped[Decimal | None] = mapped_column(Numeric(12, 4))

    # Profitability and balance-sheet ratios
    gross_margin: Mapped[Decimal | None] = mapped_column(Numeric(8, 4))
    operating_margin: Mapped[Decimal | None] = mapped_column(Numeric(8, 4))
    return_on_equity: Mapped[Decimal | None] = mapped_column(Numeric(8, 4))
    debt_to_equity: Mapped[Decimal | None] = mapped_column(Numeric(12, 4))
    current_ratio: Mapped[Decimal | None] = mapped_column(Numeric(12, 4))

    # Valuation ratios
    price_to_earnings: Mapped[Decimal | None] = mapped_column(Numeric(12, 4))
    price_to_book: Mapped[Decimal | None] = mapped_column(Numeric(12, 4))
    price_to_sales: Mapped[Decimal | None] = mapped_column(Numeric(12, 4))

    # Python-side link back to the related company
    company: Mapped["Company"] = relationship(
        back_populates="financial_snapshots",
    )