from fastapi import FastAPI

from app.routers.root import router as root_router
from app.routers.health import router as health_router


app = FastAPI(
    title="SALIKSIK API",
    description=(
        "An AI-powered investment intelligence platform that helps "
        "beginner investors research stocks, manage portfolios, "
        "and make informed investment decisions."
    ),
    version="0.1.0",
)

app.include_router(root_router)
app.include_router(health_router)