"""
Provider-independent company-directory record.
"""

from dataclasses import dataclass

@dataclass
class NormalizedCompanyDirectoryEntry:
    cik: int
    ticker: str
    company_name: str
    exchange: str | None
    country: str | None = "United States"
    source: str = "SEC"