from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from app.routers import products, categories, sms
import os

STAGE = os.environ['STAGE']
root_path = '/' if not STAGE else f'/{STAGE}'

app = FastAPI(
    title="Inter-Price-The-Supermarket-Comparator",
    root_path=root_path
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-type", "Access-Control-Allow-Origin", "Access-Control-Allow-Credentials"],
)

app.include_router(products.router, tags=["Products"])
app.include_router(categories.router, tags=['Categories'])
app.include_router(sms.router, tags=["SMS"])

@app.get('/')
async def root():
    return {"data": "Hello from Interprice!"}

handler = Mangum(app)