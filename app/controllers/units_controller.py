from typing import List
from fastapi import APIRouter, HTTPException

from app.models.unit import Unit
from app.schemas.unit import UnitCreate, UnitRead, UnitUpdate
from app.services.unit_service import UnitService

router = APIRouter()

@router.post("/", response_model=UnitRead, status_code=201)
def create_unit(unit: UnitCreate) -> Unit:
    return UnitService.create_unit(unit)

@router.get("/{unit_id}", response_model=UnitRead)
def get_unit(unit_id: str) -> Unit:
    unit = UnitService.get_unit(unit_id)
    if not unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    return unit

@router.get("/", response_model=List[UnitRead])
def list_units() -> list[Unit]:
    return UnitService.list_units()

@router.patch("/{unit_id}", response_model=UnitRead)
def update_unit(unit_id: str, unit: UnitUpdate) -> Unit:
    updated_unit = UnitService.update_unit(unit_id, unit)
    if not updated_unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    return updated_unit
