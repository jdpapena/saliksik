from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {
        "app": "SALIKSIK API",
        "version": "0.1.0",
        "status": "running",
        "docs": "/docs"
    }