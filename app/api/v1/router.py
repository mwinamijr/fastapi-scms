from fastapi import APIRouter
from app.modules.health.router import router as health_router
from app.modules.identity.routers.user import router as user_router
from app.modules.identity.routers.school import router as school_router

api_router = APIRouter()

api_router.include_router(health_router, prefix="/health", tags=["Health"])
api_router.include_router(school_router, prefix="/schools", tags=["Schools"])
api_router.include_router(user_router, prefix="/users", tags=["Users"])
