"""Provide a simple API health-check endpoint."""

from fastapi import APIRouter

router = APIRouter(tags=["Health"])

@router.get("/health")
def read_health() -> dict[str, str]:
    """Confirm that the API process is running."""

    return {
        "status": "healthy",
    }