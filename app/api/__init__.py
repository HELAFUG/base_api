from fastapi import APIRouter
from core.config import settings
from .api_v1 import v1_router

api_router = APIRouter(prefix=settings.api.prefix)
api_router.include_router(v1_router)
