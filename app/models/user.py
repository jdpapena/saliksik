"""
Stores account information for people using SALIKSIK.

- Only a secure password hash will be saved.
"""

# Standard library imports
from datetime import datetime

# Third-party imports
from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Local imports
from app.database.base import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.investor_profile import InvestorProfile
    from app.models.saved_company import SavedCompany
    from app.models.comparison_history import ComparisonHistory

class User(Base):
    """Represents one registered SALIKSIK user."""

    __tablename__ = "users"

    # Primary key
    id: Mapped[int] = mapped_column(primary_key=True)

    # Login details
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
    )
    password_hash: Mapped[str] = mapped_column(String(255))

    # Account status
    is_active: Mapped[bool] = mapped_column(default=True)

    # Account creation timestamp
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    # Saved profile about user
    investor_profile: Mapped["InvestorProfile | None"] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
        uselist=False,
    )

    # Companies bookmarked by this user
    saved_companies: Mapped[list["SavedCompany"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )

    # Previous company comparisons by this user
    comparison_history: Mapped[list["ComparisonHistory"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )