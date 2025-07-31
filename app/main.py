from fastapi import FastAPI
from app.routers import shipment

app = FastAPI()
app.include_router(shipment.router, prefix="/api")

@app.get("/deneme")
def health_check():
    return {"status": "ok"}
