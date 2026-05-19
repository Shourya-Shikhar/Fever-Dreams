from fastapi import APIRouter
from .endpoints import personas

api_router = APIRouter()
api_router.include_router(personas.router, prefix="/personas", tags=["personas"])