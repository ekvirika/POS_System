from typing import List, Optional
from app.db.database import db_session
from app.models.unit import Unit
from app.schemas.unit import UnitCreate, UnitUpdate


class UnitService:
    @staticmethod
    def create_unit(data: UnitCreate) -> Unit:
        unit = Unit(**data.dict())
        with db_session() as session:
            session.add(unit)
            session.commit()
            session.refresh(unit)
        return unit

    @staticmethod
    def get_unit(unit_id: str) -> Optional[Unit]:
        with db_session() as session:
            return session.query(Unit).filter(Unit.id == unit_id).first()

    @staticmethod
    def list_units() -> List[Unit]:
        with db_session() as session:
            return session.query(Unit).all()

    @staticmethod
    def update_unit(unit_id: str, data: UnitUpdate) -> Optional[Unit]:
        with db_session() as session:
            unit = session.query(Unit).filter(Unit.id == unit_id).first()
            if not unit:
                return None
            for key, value in data.dict(exclude_unset=True).items():
                setattr(unit, key, value)
            session.commit()
            return unit
