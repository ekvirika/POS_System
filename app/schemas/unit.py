from pydantic import BaseModel


class UnitCreate(BaseModel):
    id: str
    name: str

class UnitRead(UnitCreate):
    pass

class UnitUpdate(BaseModel):
    name: str
