from typing import List, Optional
from datetime import date

from pydantic import BaseModel

class Price(BaseModel):
    price: float
    price_per_unit: float
    updated: date 

    class Config:
        orm_mode = True

class Details(BaseModel):
    subcategory: Optional[str]
    net_qty: Optional[str]
    ingredients: Optional[str]
    storage: Optional[str]
    preparation: Optional[str]
    manufacturer: Optional[str]
    
    class Config:
        orm_mode = True

class SuperMarketCategory(BaseModel):
    supermarket: str
    categories: List[str]

    class Config:
        orm_mode = True

class Product(BaseModel):
    product_id: int
    supermarket: str
    name: str
    category: str
    image_url: str
    image_url_s3: str
    prices: List[Price]

    class Config:
        orm_mode = True

class ProductDetails(Product):
    details: Optional[Details]

    class Config:
        orm_mode = True

class SMS(BaseModel):
    number: str
    message: str

class verifySMS(BaseModel):
    number: str
    password: str
