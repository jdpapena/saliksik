"""
Provider-independent historical price structure.
"""

from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class NormalizedHistoricalPrice:
    
    """One daily market-price record."""
    price_date: date
    open_price: Decimal | None
    high_price: Decimal | None
    low_price: Decimal | None
    close_price: Decimal
    volume: int | None