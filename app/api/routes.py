#FastAPI Router
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.auth_service import AuthService
from app.repositories.user_repository import UserRepository
from app.domain.auth_strategy import JWTStrategy, SessionStrategy

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str
    method: str # "jwt" o "session"

@router.post("/login")
def login(data: LoginRequest):
    repo = UserRepository()

    if data.method == "jwt":
        strategy = JWTStrategy()
    elif data.method == "session":
        strategy = SessionStrategy()
    else:
        raise HTTPException(status_code=400, detail="Uknown method")

    auth_service = AuthService(strategy, repo)

    try:
        token = auth_service.login(data.username, data.password)
        return {"token": token}
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))