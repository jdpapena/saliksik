"""
Stores raw financial facts reported by a company for one
annual or quarterly reporting period.
"""

from datetime import date
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import (
    Date,
    ForeignKey,
    Integer,
    Numeric,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.models.company import Company


class FinancialSnapshot(Base):
    """Stores raw financial facts for one reporting period."""
    __tablename__ = "financial_snapshots"

    # Prevent duplicate reports for the same company and period.
    __table_args__ = (
        UniqueConstraint(
            "company_id",
            "fiscal_year",
            "fiscal_period",
            name="uq_financial_snapshot_company_period",
        ),
    )

    # Primary key
    id: Mapped[int] = mapped_column(primary_key=True)

    # Company connected to this report
    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id"),
        nullable=False,
        index=True,
    )

    # Reporting period
    fiscal_year: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    fiscal_period: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )
    report_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        index=True,
    )
    filing_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    # Currency used in the financial report
    currency: Mapped[str | None] = mapped_column(
        String(10),
        nullable=True,
    )

    # Income statement facts
    revenue: Mapped[Decimal | None] = mapped_column(
        Numeric(24, 2),
        nullable=True,
    )
    gross_profit: Mapped[Decimal | None] = mapped_column(
        Numeric(24, 2),
        nullable=True,
    )
    operating_income: Mapped[Decimal | None] = mapped_column(
        Numeric(24, 2),
        nullable=True,
    )
    net_income: Mapped[Decimal | None] = mapped_column(
        Numeric(24, 2),
        nullable=True,
    )
    earnings_per_share: Mapped[Decimal | None] = mapped_column(
        Numeric(16, 4),
        nullable=True,
    )

    # Balance-sheet facts
    cash_and_equivalents: Mapped[Decimal | None] = mapped_column(
        Numeric(24, 2),
        nullable=True,
    )
    current_assets: Mapped[Decimal | None] = mapped_column(
        Numeric(24, 2),
        nullable=True,
    )
    total_assets: Mapped[Decimal | None] = mapped_column(
        Numeric(24, 2),
        nullable=True,
    )
    current_liabilities: Mapped[Decimal | None] = mapped_column(
        Numeric(24, 2),
        nullable=True,
    )
    total_liabilities: Mapped[Decimal | None] = mapped_column(
        Numeric(24, 2),
        nullable=True,
    )
    total_debt: Mapped[Decimal | None] = mapped_column(
        Numeric(24, 2),
        nullable=True,
    )
    shareholders_equity: Mapped[Decimal | None] = mapped_column(
        Numeric(24, 2),
        nullable=True,
    )
    shares_outstanding: Mapped[Decimal | None] = mapped_column(
        Numeric(24, 2),
        nullable=True,
    )

    # Cash-flow statement facts
    operating_cash_flow: Mapped[Decimal | None] = mapped_column(
        Numeric(24, 2),
        nullable=True,
    )
    capital_expenditure: Mapped[Decimal | None] = mapped_column(
        Numeric(24, 2),
        nullable=True,
    )

    # Connection back to the company
    company: Mapped["Company"] = relationship(
        back_populates="financial_snapshots",
    )