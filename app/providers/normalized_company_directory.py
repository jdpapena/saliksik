"""Define a provider-independent company-directory record."""

from dataclasses import dataclass

@dataclass
class NormalizedCompanyDirectoryEntry:
    """Store one normalized ticker entry before database saving."""

    cik: int
    ticker: str
    company_name: str
    exchange: str | None
    country: str | None = "United States"
    source: str = "SEC"