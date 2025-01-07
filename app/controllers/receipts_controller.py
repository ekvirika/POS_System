from fastapi import APIRouter, HTTPException
from app.services.receipt_service import ReceiptService
from app.schemas.receipt import ReceiptCreate, ReceiptRead, ReceiptUpdate

router = APIRouter()

@router.post("/", response_model=ReceiptRead, status_code=201)
def create_receipt(receipt: ReceiptCreate):
    return ReceiptService.create_receipt(receipt)

@router.get("/{receipt_id}", response_model=ReceiptRead)
def get_receipt(receipt_id: str):
    receipt = ReceiptService.get_receipt(receipt_id)
    if not receipt:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return receipt

@router.get("/", response_model=list[ReceiptRead])
def list_receipts():
    return ReceiptService.list_receipts()

@router.patch("/{receipt_id}", response_model=ReceiptRead)
def update_receipt(receipt_id: str, receipt: ReceiptUpdate):
    return ReceiptService.update_receipt(receipt_id, receipt)
