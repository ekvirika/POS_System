from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Unit(Base):
    __tablename__ = 'units'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
