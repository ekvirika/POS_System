from typing import List
from fastapi import APIRouter, HTTPException

from app.models.receipt import Receipt
from app.schemas.receipt import ReceiptCreate, ReceiptRead, ReceiptUpdate
from app.services.receipt_service import ReceiptService

router = APIRouter()

@router.post("/", response_model=ReceiptRead, status_code=201)
def create_receipt(receipt: ReceiptCreate) -> Receipt:
    return ReceiptService.create_receipt(receipt)

@router.get("/{receipt_id}", response_model=ReceiptRead)
def get_receipt(receipt_id: str) -> Receipt:
    receipt = ReceiptService.get_receipt(receipt_id)
    if not receipt:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return receipt

@router.get("/", response_model=List[ReceiptRead])
def list_receipts() -> list[Receipt]:
    return ReceiptService.list_receipts()

@router.patch("/{receipt_id}", response_model=ReceiptRead)
def update_receipt(receipt_id: str, receipt: ReceiptUpdate) -> Receipt:
    updated_receipt = ReceiptService.update_receipt(receipt_id, receipt)
    if not updated_receipt:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return updated_receipt
