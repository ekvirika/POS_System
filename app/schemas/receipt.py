from pydantic import BaseModel
from datetime import datetime

class ReceiptCreate(BaseModel):
    id: str
    customer_name: str
    total_amount: int
    created_at: datetime

class ReceiptRead(ReceiptCreate):
    pass

class ReceiptUpdate(BaseModel):
    customer_name: str
    total_amount: int
