from fastapi import APIRouter

from src.config import settings
from .jwt.views import router as jwt_router

router = APIRouter()
router.include_router(router=jwt_router, prefix=settings.api_v1_prefix)
