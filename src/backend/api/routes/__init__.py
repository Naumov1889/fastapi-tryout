from fastapi import APIRouter
from .some_test_app import router as some_test_app_router

router = APIRouter()
router.include_router(some_test_app_router, prefix="/some_test_app", tags=["some_test_app"])
