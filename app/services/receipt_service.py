from app.models.receipt import Receipt
from app.db.database import db_session
from app.schemas.receipt import ReceiptCreate, ReceiptUpdate

class ReceiptService:
    @staticmethod
    def create_receipt(data: ReceiptCreate):
        receipt = Receipt(**data.dict())
        with db_session() as session:
            session.add(receipt)
            session.commit()
            session.refresh(receipt)
        return receipt

    @staticmethod
    def get_receipt(receipt_id: str):
        with db_session() as session:
            return session.query(Receipt).filter(Receipt.id == receipt_id).first()

    @staticmethod
    def list_receipts():
        with db_session() as session:
            return session.query(Receipt).all()

    @staticmethod
    def update_receipt(receipt_id: str, data: ReceiptUpdate):
        with db_session() as session:
            receipt = session.query(Receipt).filter(Receipt.id == receipt_id).first()
            if not receipt:
                return None
            for key, value in data.dict(exclude_unset=True).items():
                setattr(receipt, key, value)
            session.commit()
            return receipt
