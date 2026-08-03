"""Provide basic information about the SALIKSIK API."""

from fastapi import APIRouter

from app.core.config import settings

router = APIRouter(tags=["Root"])

@router.get("/")
def read_root() -> dict[str, str]:
    """Return basic application information."""

    return {
        "app": settings.app_name,
        "version": settings.app_version,
        "status": "running",
        "docs": "/docs",
    }