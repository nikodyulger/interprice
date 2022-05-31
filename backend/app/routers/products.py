from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from typing import List, Optional
from ..dependencies import get_db

router = APIRouter()

@router.get(
    "/products",
    response_model=List[schemas.Product],
    summary="Catalog of products"
)
async def get_products(skip: int=0, limit: int = 90, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products

@router.get(
    "/details/{supermarket}/{p_id}",
    response_model=schemas.ProductDetails,
    summary="Details of a product"
)
async def get_product(supermarket:str, p_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, p_id=p_id, supermarket=supermarket)
    if product == None:
        raise HTTPException(status_code=404, detail="Product Not Found!")
    return product

@router.get(
    "/products/search/",
    response_model=List[schemas.Product],
    summary="Filteres products by certain categories"
)
def get_filtered_products( q: str , db: Session = Depends(get_db)):
    products = crud.get_filtered_products(db, q=q)
    return products
