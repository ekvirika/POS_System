from pydantic import BaseModel

class ProductCreate(BaseModel):
    unit_id: str
    name: str
    barcode: str
    price: int

class ProductRead(ProductCreate):
    id: str

class ProductUpdate(BaseModel):
    price: int
