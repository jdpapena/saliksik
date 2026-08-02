"""
Stores company comparisons made by users.
"""

# Standard library imports
from datetime import datetime
from typing import TYPE_CHECKING

# Third-party imports
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Local imports
from app.database.base import Base

# Type checking imports
if TYPE_CHECKING:
    from app.models.user import User
    from app.models.company import Company


class ComparisonHistory(Base):
    """Represents one comparison made by a user."""

    __tablename__ = "comparison_history"

    # Primary key
    id: Mapped[int] = mapped_column(primary_key=True)

    # User who performed the comparison
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        index=True,
    )

    # First company
    company_a_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id"),
        index=True,
    )

    # Second company
    company_b_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id"),
        index=True,
    )

    # When the comparison happened
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    # Relationships
    user: Mapped["User"] = relationship(
        back_populates="comparison_history",
    )

    company_a: Mapped["Company"] = relationship(
        foreign_keys=[company_a_id],
    )

    company_b: Mapped["Company"] = relationship(
        foreign_keys=[company_b_id],
    )