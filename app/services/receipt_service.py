from typing import List, Optional
from app.db.database import db_session
from app.models.receipt import Receipt
from app.schemas.receipt import ReceiptCreate, ReceiptUpdate
from app.services.sales_service import SaleReportService


class ReceiptService:
    @staticmethod
    def create_receipt(data: ReceiptCreate) -> Receipt:
        receipt = Receipt(**data.dict())
        with db_session() as session:
            session.add(receipt)
            session.commit()
            session.refresh(receipt)
        return receipt

    @staticmethod
    def get_receipt(receipt_id: str) -> Optional[Receipt]:
        with db_session() as session:
            return session.query(Receipt).filter(Receipt.id == receipt_id).first()

    @staticmethod
    def list_receipts() -> List[Receipt]:
        with db_session() as session:
            return session.query(Receipt).all()

    @staticmethod
    def update_receipt(receipt_id: str, data: ReceiptUpdate) -> Optional[Receipt]:
        with db_session() as session:
            receipt = session.query(Receipt).filter(Receipt.id == receipt_id).first()
            if not receipt:
                return None
            for key, value in data.dict(exclude_unset=True).items():
                setattr(receipt, key, value)
            session.commit()
            return receipt

    @staticmethod
    def close_receipt(receipt_id: str) -> Optional[Receipt]:
        with db_session() as session:
            receipt = session.query(Receipt).filter(Receipt.id == receipt_id).first()
            if not receipt:
                return None
            if receipt.status == "closed":
                raise ValueError("Receipt is already closed")

            receipt.status = "closed"
            session.commit()

            # Update sales report
            SaleReportService.update_sales_report(
                n_receipts=1,
                revenue=receipt.total_amount
            )
            return receipt
