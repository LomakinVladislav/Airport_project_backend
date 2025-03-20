from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(route.router,prefix="", tags=["Database_route"])
