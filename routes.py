from fastapi import APIRouter, Depends
from app.auth.jwt_validator import validate_token
from app.payments.service import create_payment

router = APIRouter()

@router.post("/")
def create(payment: dict, user=Depends(validate_token)):
    return create_payment(payment, user)
