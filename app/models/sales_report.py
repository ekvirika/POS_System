from sqlalchemy import Column, Integer

from app.db.database import Base


class SaleReport(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, autoincrement=True)
    n_receipts = Column(Integer, default=0, nullable=False)
    revenue = Column(Integer, default=0, nullable=False)
