import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# URL of the frontend app
origins = [
    "https://localhost:8100"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = False,
    allow_methods = ["*"],
    allow_headers =["*"]
)
@app.get('/')
async def root():
    return {"data": "Hello!"}

@app.get('/promos')
async def get_ofertas():
    with open('promos.json') as f:
        promos = json.load(f)
    response = []
    id = 0 
    for promo in promos:
        response.append(
            {   
                "id": id,
                "name": promo['name'],
                "price": promo['price'],
                "url": f"images/{ promo['images'][0]['path'] }" #directory of static images in frontend
            }
        )
        id += 1
    return response