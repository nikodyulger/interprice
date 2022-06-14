from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from typing import List
from ..dependencies import get_db

router = APIRouter()

@router.get(
    "/categories/",
    response_model=List[schemas.SuperMarketCategory],
    summary="Categories of Products by Supermarket"
)
def get_categories(db: Session = Depends(get_db)):
    d = dict()
    response = []
    for s,c in crud.get_categories(db):
        d.setdefault(s,[]).append(c)
    for k in d:
        response.append({
            "supermarket": k,
            "categories": d[k]
        })
    return response

