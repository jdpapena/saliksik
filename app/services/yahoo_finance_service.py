from fastapi import HTTPException
import yfinance as yf

from app.models.yahoo_stock import YahooStock

def get_stock_info(ticker: str) -> YahooStock:
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        if not info.get("longName"):
            raise HTTPException(
                status_code=404,
                detail=f"Ticker '{ticker.upper()}' was not found."
            )

        return YahooStock(
            ticker=ticker.upper(),
            company_name=info.get("longName"),
            sector=info.get("sector"),
            market_cap=info.get("marketCap"),
            pe_ratio=info.get("trailingPE"),
            beta=info.get("beta"),      
            free_cash_flow=info.get("freeCashflow"),  
            
            # Financial Health
            current_ratio=info.get("currentRatio"),
            debt_to_equity=(
                info.get("debtToEquity") / 100
                if info.get("debtToEquity") is not None
                else None
            ),
            return_on_equity=(
                info.get("returnOnEquity") * 100
                if info.get("returnOnEquity") is not None
                else None
            ),
            profit_margins=(
                info.get("profitMargins") * 100
                if info.get("profitMargins") is not None
                else None
            ),

            # Growth
            revenue_growth=(
                info.get("revenueGrowth") * 100
                if info.get("revenueGrowth") is not None
                else None
            ),
            earnings_growth=(
                info.get("earningsGrowth") * 100
                if info.get("earningsGrowth") is not None
                else None
            ),

            # Market Sentiment
            recommendation_mean=info.get("recommendationMean"),
            recommendation_key=info.get("recommendationKey"),

            number_of_analyst_opinions=info.get("numberOfAnalystOpinions"),
        )
    
    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Unable to retrieve stock data from Yahoo Finance."
        )