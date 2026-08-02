"""
Stores the user's investing preferences and onboarding details.
"""

from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.models.user import User


class InvestorProfile(Base):
    """Represents one user's investor profile."""

    __tablename__ = "investor_profiles"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
        index=True,
    )

    goal: Mapped[str] = mapped_column(String(100))

    monthly_savings: Mapped[Decimal] = mapped_column(
        Numeric(12, 2)
    )

    investment_horizon_years: Mapped[int]

    checking_frequency: Mapped[str] = mapped_column(
        String(20)
    )

    investor_style: Mapped[str] = mapped_column(
        String(50)
    )

    experience_level: Mapped[str] = mapped_column(
        String(30)
    )

    user: Mapped["User"] = relationship(
        back_populates="investor_profile"
    )