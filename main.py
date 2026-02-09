from fastapi import FastAPI
from app.payments.routes import router as payment_router

app = FastAPI(title="Secure Payment API")

app.include_router(payment_router, prefix="/payments")
