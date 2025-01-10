from typing import List
from fastapi import APIRouter, HTTPException

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductRead, ProductUpdate
from app.services.product_service import ProductService

router = APIRouter()

@router.post("/", response_model=ProductRead, status_code=201)
def create_product(product: ProductCreate) -> Product:
    return ProductService.create_product(product)

@router.get("/{product_id}", response_model=ProductRead)
def get_product(product_id: str) -> Product:
    product = ProductService.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/", response_model=List[ProductRead])
def list_products() -> list[Product]:
    return ProductService.list_products()

@router.patch("/{product_id}", response_model=ProductRead)
def update_product(product_id: str, product: ProductUpdate) -> Product:
    updated_product = ProductService.update_product(product_id, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product
