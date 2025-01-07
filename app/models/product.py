from sqlalchemy import Column, String, Integer, ForeignKey
from app.db.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    barcode = Column(String, unique=True, nullable=False)
    price = Column(Integer, nullable=False)
    unit_id = Column(String, ForeignKey("units.id"), nullable=False)
