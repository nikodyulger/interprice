from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app import crud, schemas
from typing import List, Optional
from ..dependencies import get_db

router = APIRouter()

@router.get(
    "/products/",
    response_model=List[schemas.Product],
    summary="Catalog of products"
)
async def get_products(skip: int=0, limit: int = 100, q_name: Optional[str] = None, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit, q_name=q_name)
    return products

@router.get(
    "/products/{supermarket}/{p_id}",
    response_model=schemas.ProductDetails,
    summary="Details of a product"
)
async def get_product(supermarket:str, p_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, p_id=p_id, supermarket=supermarket)
    if product == None:
        raise HTTPException(status_code=404, detail="Product Not Found!")
    return product

@router.get(
    "/products/filters/",
    response_model=List[schemas.Product],
    summary="Filteres products by certain categories"
)
def get_filtered_products( cat: Optional[List[str]] = Query(None), sup: Optional[List[str]] = Query(None), db: Session = Depends(get_db)):
    products = crud.get_filtered_products(db, cat=cat, sup=sup)
    return products
