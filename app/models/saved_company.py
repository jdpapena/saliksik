"""
Stores companies bookmarked by users for future research.
"""

# Standard library imports
from datetime import datetime
from typing import TYPE_CHECKING

# Third-party imports
from sqlalchemy import DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Local imports
from app.database.base import Base

# Type checking imports
if TYPE_CHECKING:
    from app.models.user import User
    from app.models.company import Company


class SavedCompany(Base):
    """Represents one bookmarked company."""

    __tablename__ = "saved_companies"

    # Prevent duplicate bookmarks
    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "company_id",
            name="uq_saved_company",
        ),
    )

    # Primary key
    id: Mapped[int] = mapped_column(primary_key=True)

    # Foreign keys
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        index=True,
    )

    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id"),
        index=True,
    )

    # When the company was saved
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    # Relationships
    user: Mapped["User"] = relationship(
        back_populates="saved_companies",
    )

    company: Mapped["Company"] = relationship(
        back_populates="saved_by_users",
    )