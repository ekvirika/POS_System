from sqlalchemy.orm import Session
from app.models import Unit

class UnitRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_unit(self, name: str) -> Unit:
        unit = Unit(name=name)
        self.db.add(unit)
        self.db.commit()
        self.db.refresh(unit)
        return unit

    def get_unit_by_id(self, unit_id: str) -> Unit:
        return self.db.query(Unit).filter(Unit.id == unit_id).first()
