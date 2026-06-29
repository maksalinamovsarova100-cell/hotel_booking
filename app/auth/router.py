from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from app.auth.dependencies import get_auth_service
from app.auth.schemas import (
    RegisterRequest,
    TokenResponse,
)
from app.auth.service import AuthService
from app.auth.schemas import (
    LoginRequest,
    TokenResponse,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
)
async def register(
    data: RegisterRequest,
    service: AuthService = Depends(get_auth_service),
):
    user = await service.register(
        email=data.email,
        username=data.username,
        password=data.password,
    )

    return user

@router.post(
    "/login",
    response_model=TokenResponse,
)
async def login(
    data: LoginRequest,
    service: AuthService = Depends(get_auth_service),
):
    token = await service.login(
        email=data.email,
        password=data.password,
    )

    return TokenResponse(
        access_token=token,
    )