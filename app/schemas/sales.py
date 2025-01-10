from pydantic import BaseModel


class SaleReportRead(BaseModel):
    n_receipts: int
    revenue: int

    class Config:
        orm_mode = True
