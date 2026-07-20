import yfinance as yf

from app.models.profile import CompanyProfile

def get_company_profile(ticker: str) -> CompanyProfile:

    stock = yf.Ticker(ticker)
    info = stock.info

    market_cap = info.get("marketCap")

    return CompanyProfile(
        ticker = ticker.upper(),
        company_name = info.get("longName"),

        description = info.get("longBusinessSummary"),

        sector = info.get("sector"),
        industry = info.get("industry"),

        ceo = info.get("companyOfficers", [{}])[0].get("name"),

        employees = info.get("fullTimeEmployees"),

        country = info.get("country"),
        city = info.get("city"),

        website = info.get("website"),

        market_cap = market_cap,
        market_cap_category = get_market_cap_category(market_cap),
    )


def get_market_cap_category(market_cap: int | None) -> str | None:
    # Source: https://www.financestrategists.com/wealth-management/stocks/market-cap/market-capitalization-categories/
    if market_cap is None:
        return None

    if market_cap >= 200_000_000_000:
        return "Mega Cap"

    if market_cap >= 10_000_000_000:
        return "Large Cap"

    if market_cap >= 2_000_000_000:
        return "Mid Cap"

    if market_cap >= 300_000_000:
        return "Small Cap"

    if market_cap >= 50_000_000:
        return "Micro Cap"

    return "Nano Cap"