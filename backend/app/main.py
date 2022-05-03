from fastapi import FastAPI
from mangum import Mangum
from app.routers import products, categories

app = FastAPI(
    title="Inter-Price-The-Supermarket-Comparator"
)

app.include_router(products.router, tags=["Products"])
app.include_router(categories.router, tags=['Categories'])

@app.get('/')
async def root():
    return {"data": "Hello from Interprice!"}

handler = Mangum(app)