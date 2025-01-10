from typing import Optional
from app.db.database import db_session
from app.models.sales_report import SaleReport


class SaleReportService:
    @staticmethod
    def get_sales_report() -> SaleReport:
        with db_session() as session:
            # Get the first sales report
            report = session.query(SaleReport).first()
            if not report:
                # Initialize the sales report if it doesn't exist
                report = SaleReport(n_receipts=0, revenue=0)
                session.add(report)
                session.commit()
                session.refresh(report)
            return report

    @staticmethod
    def update_sales_report(n_receipts: int, revenue: int) -> SaleReport:
        with db_session() as session:
            # Get the first sales report
            report = session.query(SaleReport).first()
            if not report:
                # Initialize the sales report if it doesn't exist
                report = SaleReport(n_receipts=n_receipts, revenue=revenue)
                session.add(report)
            else:
                # Update the existing report with new values
                report.n_receipts += n_receipts
                report.revenue += revenue
            session.commit()
            return report
