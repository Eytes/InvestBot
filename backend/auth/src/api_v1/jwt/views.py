from fastapi import APIRouter, status

from src.api_v1.jwt.schemas import Token

router = APIRouter(tags=["JWT"])


@router.post(
    path="/login",
    status_code=status.HTTP_201_CREATED,
    response_model=Token,
)
def login_and_get_jwt():
    """Выдача токена после успешной аутентификации"""
    return Token(
        access="test_token",
        type="Bearer",
    )
