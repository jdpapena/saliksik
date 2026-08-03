"""Create and configure the SALIKSIK FastAPI application."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routers.company import router as company_router
from app.routers.health import router as health_router
from app.routers.root import router as root_router

app = FastAPI(
    title=settings.app_name,
    description=(
        "A financial research platform that helps beginner investors "
        "discover and compare companies using reported financial facts."
    ),
    version=settings.app_version,
)

# Allow the configured frontend to access the API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register the API.
app.include_router(root_router)
app.include_router(health_router)
app.include_router(company_router)