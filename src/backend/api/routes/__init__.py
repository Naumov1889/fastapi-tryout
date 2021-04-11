from fastapi import APIRouter
from .cleanings import router as cleanings_router

router = APIRouter()
router.include_router(cleanings_router, prefix="/cleanings", tags=["cleanings"])
