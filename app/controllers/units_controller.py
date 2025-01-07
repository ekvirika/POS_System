from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.services.unit_service import UnitService
from app.repositories.unit_repository import UnitRepository

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/units")
def create_unit(name: str, db: Session = Depends(get_db)):
    service = UnitService(UnitRepository(db))
    return {"unit": service.create_unit(name)}
