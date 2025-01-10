from sqlalchemy import Column, DateTime, Integer, String

from app.db.database import Base


class Receipt(Base):
    __tablename__ = "receipts"

    id = Column(String, primary_key=True)
    customer_name = Column(String, nullable=False)
    total_amount = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
