from fastapi import FastAPI

from app.routers.root import router as root_router
from app.routers.health import router as health_router
from app.routers.stocks import router as stocks_router
from app.routers.company import router as company_router

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="SALIKSIK API",
    description=(
        "An AI-powered investment intelligence platform that helps "
        "beginner investors research stocks, manage portfolios, "
        "and make informed investment decisions."
    ),
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(root_router)
app.include_router(health_router)
app.include_router(stocks_router)
app.include_router(company_router)