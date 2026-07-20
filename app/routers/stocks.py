from fastapi import APIRouter

from app.models.analysis import StockAnalysis
from app.models.yahoo_stock import YahooStock
from app.models.history import HistoricalPrice
from app.services.stock_service import analyze_stock
from app.services.yahoo_finance_service import get_stock_info
from app.services.yahoo_finance_service import get_stock_info
from app.services.history_service import get_stock_history
from app.models.profile import CompanyProfile
from app.services.profile_service import get_company_profile
from app.models.performance import StockPerformance
from app.services.performance_service import get_stock_performance
from app.models.news import StockNews
from app.services.news_service import get_stock_news
from app.models.summary import StockSummary
from app.services.summary_service import generate_summary

router = APIRouter(prefix="/stocks", tags=["Stocks"])

@router.get("/{symbol}", response_model=YahooStock)
def read_stock(symbol: str):
    return get_stock_info(symbol)

@router.get("/{symbol}/analysis", response_model=StockAnalysis)
def read_stock_analysis(symbol: str):
    return analyze_stock(symbol)

@router.get("/{symbol}/history", response_model=list[HistoricalPrice])
def read_stock_history(symbol: str, period: str = "1y"):
    return get_stock_history(symbol, period)

@router.get("/{symbol}/profile", response_model=CompanyProfile)
def read_company_profile(symbol: str):
    return get_company_profile(symbol)

@router.get("/{symbol}/performance", response_model=StockPerformance)
def read_stock_performance(symbol: str):
    return get_stock_performance(symbol)

@router.get("/{symbol}/news", response_model=StockNews)
def read_stock_news(symbol: str):
    return get_stock_news(symbol)

@router.get("/{symbol}/summary", response_model=StockSummary)
def read_stock_summary(symbol: str):
    analysis = analyze_stock(symbol)
    return generate_summary(ticker = analysis.ticker, company_name = analysis.company_name, score = analysis.score)
