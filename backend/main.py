import json

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# URL of the frontend app
origins = [
    "https://localhost:8100"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
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
    for promo in promos:
        response.append(
            {
                "name": promo['name'],
                "precio": promo['price'],
                "url": f"images/{ promo['images'][0]['path'] }" #directory of static images in frontend
            }
        )
    return json.dumps(response)