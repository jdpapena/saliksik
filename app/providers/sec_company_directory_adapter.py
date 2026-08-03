"""Normalize the SEC company ticker directory."""

from app.providers.normalized_company_directory import (
    NormalizedCompanyDirectoryEntry,
)

class SecCompanyDirectoryAdapter:
    """Convert SEC directory rows into SALIKSIK records."""

    def normalize(
        self,
        raw_data: dict,
    ) -> list[NormalizedCompanyDirectoryEntry]:
        """Return normalized company-directory entries."""

        fields = raw_data.get("fields", [])
        rows = raw_data.get("data", [])

        if not fields or not rows:
            return []

        # Map each SEC field name to its position in every row.
        field_indexes = {
            field_name: index
            for index, field_name in enumerate(fields)
        }

        required_fields = {
            "cik",
            "name",
            "ticker",
            "exchange",
        }

        if not required_fields.issubset(field_indexes):
            return []

        entries: list[NormalizedCompanyDirectoryEntry] = []

        for row in rows:
            ticker = str(
                row[field_indexes["ticker"]]
            ).strip().upper()

            company_name = str(
                row[field_indexes["name"]]
            ).strip()

            exchange_value = row[field_indexes["exchange"]]

            exchange = (
                str(exchange_value).strip()
                if exchange_value
                else None
            )

            # Skip entries that cannot be searched or identified.
            if not ticker or not company_name:
                continue

            entries.append(
                NormalizedCompanyDirectoryEntry(
                    cik=int(row[field_indexes["cik"]]),
                    ticker=ticker,
                    company_name=company_name,
                    exchange=exchange,
                )
            )

        return entries