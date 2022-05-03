from fastapi import FastAPI
from mangum import Mangum
from app.routers import products, categories
import os

STAGE = os.environ['STAGE']
root_path = '/' if not STAGE else f'/{STAGE}'

app = FastAPI(
    title="Inter-Price-The-Supermarket-Comparator",
    root_path=root_path
)

app.include_router(products.router, tags=["Products"])
app.include_router(categories.router, tags=['Categories'])

@app.get('/')
async def root():
    return {"data": "Hello from Interprice!"}

handler = Mangum(app)