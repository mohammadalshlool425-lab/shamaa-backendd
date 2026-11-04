from fastapi import FastAPI

from app.routes import products_api, users_api

app = FastAPI(
    title="Shamaa API",
    description="C2C/B2C Marketplace API for Yarmouk University & Irbid",
    version="1.0.0",
)

app.include_router(users_api.router)
app.include_router(products_api.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to Shamaa API - The Heart of Yarmouk University Marketplace!"}
