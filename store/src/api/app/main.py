from fastapi import FastAPI
from app.routers import products, users, orders

app = FastAPI()

app.include_router(products.router)
app.include_router(users.router)
app.include_router(orders.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}