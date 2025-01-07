from sqlalchemy import Column, String
from app.db.database import Base

class Unit(Base):
    __tablename__ = "units"

    id = Column(String, primary_key=True)
    name = Column(String, unique=True, nullable=False)
