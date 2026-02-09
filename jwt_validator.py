from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer
import jwt

security = HTTPBearer()

def validate_token(credentials = Security(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(
            token,
            options={"verify_signature": False}
        )
        return payload
    except Exception:
        raise HTTPException(status_code=401, detail="Token inválido")
