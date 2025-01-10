from typing import List, Optional

from app.db.database import db_session
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


class ProductService:
    @staticmethod
    def create_product(data: ProductCreate) -> Product:
        product = Product(**data.dict())
        with db_session() as session:
            session.add(product)
            session.commit()
            session.refresh(product)
        return product

    @staticmethod
    def get_product(product_id: str) -> Optional[Product]:
        with db_session() as session:
            return session.query(Product).filter(Product.id == product_id).first()

    @staticmethod
    def list_products() -> List[Product]:
        with db_session() as session:
            return session.query(Product).all()

    @staticmethod
    def update_product(product_id: str, data: ProductUpdate) -> Optional[Product]:
        with db_session() as session:
            product = session.query(Product).filter(Product.id == product_id).first()
            if not product:
                return None
            for key, value in data.dict(exclude_unset=True).items():
                setattr(product, key, value)
            session.commit()
            return product
