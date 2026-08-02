"""
Check saved annual financial snapshots.
"""

from app.database import SessionLocal
from app.models.company import Company
from app.models.financial_snapshot import FinancialSnapshot

database = SessionLocal()

try:
    company = (
        database.query(Company)
        .filter(Company.ticker == "AAPL")
        .first()
    )

    if company is None:
        print("AAPL not found.")
    else:
        snapshots = (
            database.query(FinancialSnapshot)
            .filter(FinancialSnapshot.company_id == company.id)
            .order_by(FinancialSnapshot.fiscal_year)
            .all()
        )

        for snapshot in snapshots[-5:]:
            print(
                snapshot.fiscal_year,
                snapshot.report_date,
                snapshot.revenue,
            )
finally:
    database.close()