from fastapi import APIRouter, HTTPException
from app.services.unit_service import UnitService
from app.schemas.unit import UnitCreate, UnitRead, UnitUpdate

router = APIRouter()

@router.post("/", response_model=UnitRead, status_code=201)
def create_unit(unit: UnitCreate):
    return UnitService.create_unit(unit)

@router.get("/{unit_id}", response_model=UnitRead)
def get_unit(unit_id: str):
    unit = UnitService.get_unit(unit_id)
    if not unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    return unit

@router.get("/", response_model=list[UnitRead])
def list_units():
    return UnitService.list_units()

@router.patch("/{unit_id}", response_model=UnitRead)
def update_unit(unit_id: str, unit: UnitUpdate):
    return UnitService.update_unit(unit_id, unit)
