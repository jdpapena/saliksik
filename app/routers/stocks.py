from fastapi import APIRouter

from app.models.analysis import StockAnalysis
from app.models.yahoo_stock import YahooStock
from app.services.stock_service import analyze_stock
from app.services.yahoo_finance_service import get_stock_info
from app.services.yahoo_finance_service import get_stock_info

router = APIRouter(
    prefix="/stocks",
    tags=["Stocks"],
)

@router.get("/{symbol}", response_model=YahooStock)
def read_stock(symbol: str):
    return get_stock_info(symbol)

@router.get("/{symbol}/analysis", response_model=StockAnalysis)
def read_stock_analysis(symbol: str):
    return analyze_stock(symbol)
