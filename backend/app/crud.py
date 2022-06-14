from jmespath import search
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func 
from .models import Product


def get_product(db: Session, p_id: int, supermarket: str):
    return db.query(Product).filter(Product.product_id == p_id and Product.supermarket == supermarket).first()


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).order_by(func.rand()).offset(skip).limit(limit).all()


def get_categories(db: Session):
    return db.query(Product.supermarket, Product.category).distinct(Product.category).all()


def get_filtered_products(db: Session, q: str):
    return db.query(Product).filter(Product.name.contains(q)).all()
