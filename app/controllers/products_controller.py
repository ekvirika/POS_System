from fastapi import APIRouter, HTTPException
from app.services.product_service import ProductService
from app.schemas.product import ProductCreate, ProductRead, ProductUpdate

router = APIRouter()

@router.post("/", response_model=ProductRead, status_code=201)
def create_product(product: ProductCreate):
    return ProductService.create_product(product)

@router.get("/{product_id}", response_model=ProductRead)
def get_product(product_id: str):
    product = ProductService.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/", response_model=list[ProductRead])
def list_products():
    return ProductService.list_products()

@router.patch("/{product_id}", response_model=ProductRead)
def update_product(product_id: str, product: ProductUpdate):
    return ProductService.update_product(product_id, product)
