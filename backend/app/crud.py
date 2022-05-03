from sqlalchemy.orm import Session
from sqlalchemy import and_
from typing import List
from .models import Product


def get_product(db: Session, p_id: int, supermarket: str):
    return db.query(Product).filter(Product.product_id == p_id and Product.supermarket == supermarket).first()

def get_products(db: Session, skip: int = 0, limit: int = 100, q_name: str = None):
    if q_name:
        return db.query(Product).filter(Product.name.contains(q_name)).offset(skip).limit(limit).all()
    else:
        return db.query(Product).offset(skip).limit(limit).all()

def get_categories(db: Session):
    return db.query(Product.supermarket,Product.category).distinct(Product.category).all()

def get_filtered_products(db: Session, cat: List[str] = None, sup: List[str] = None):
    if cat == None and sup != None:
        return  db.query(Product).filter(Product.supermarket.in_(sup)).all()
    elif cat != None and sup == None:
        return  db.query(Product).filter(Product.category.in_(cat)).all()
    else:
        return db.query(Product).filter(and_(Product.category.in_(cat), Product.supermarket.in_(sup))).all()