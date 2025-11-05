from fastapi import APIRouter
from core.config import settings
from .dependency_example import router as dependency_example_router
from .user import router as user_router

v1_router = APIRouter(prefix=settings.api.v1.prefix)
# v1_router.include_router(dependency_example_router)
v1_router.include_router(user_router)
