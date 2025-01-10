from fastapi import APIRouter

from app.schemas.sales import SaleReportRead
from app.services.sales_service import SaleReportService

router = APIRouter()

@router.get("/", response_model=SaleReportRead)
def get_sales_report() -> SaleReportRead:
    return SaleReportService.get_sales_report()