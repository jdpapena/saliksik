# SALIKSIK - AI-Powered Investment Intelligence Platform

A full-stack stock analysis platform engineered to help beginner investors evaluate publicly traded companies using quantitative financial metrics. The application retrieves market data, analyzes multiple investment factors, and presents an easy-to-understand assessment with visual ratings, company fundamentals, and investment insights.

SALIKSIK was built to practice designing a complete software system - from backend API development to frontend visualization - while applying software engineering principles such as modular architecture, RESTful APIs, strong typing, and maintainable code organization.

---

## Features
- **Fundamental Analysis:** Evaluates a company's financial health, growth, valuation, risk, and market sentiment.
- **Weighted Scoring System:** Combines multiple investment factors into a normalized overall score and star rating.
- **Company Snapshot:** Displays key company information including sector, industry, country, and market capitalization.
- **Investment Summary:** Automatically generates strengths, weaknesses, and an overall company assessment.
- **Responsive User Interface:** Clean React interface designed for beginner investors.
- **REST API Backend:** FastAPI-powered backend serving structured investment analysis.

---

## Technologies
- **Backend:** Python, FastAPI, Pydantic, Uvicorn, yfinance
- **Frontend:** React, TypeScript, Vite, Axios, Tailwind CSS

---

## How It Works
The application processes stock analysis in five stages:
1. **Market Data Retrieval**
   - Downloads company fundamentals and market information using Yahoo Finance.

2. **Financial Evaluation**
   - Calculates category scores for:
     - Financial Health
     - Growth
     - Valuation
     - Risk
     - Market Sentiment

3. **Overall Assessment**
   - Applies weighted scoring to generate an overall investment score, star rating, and qualitative assessment.

4. **Summary Generation**
   - Produces strengths, weaknesses, and a beginner-friendly company overview.

5. **Frontend Visualization**
   - Displays the analysis through reusable React components with intuitive visual indicators.

---

## Project Structure

```
SALIKSIK
├── backend
│   ├── app
│   ├── routers
│   ├── services
│   ├── models
│   └── main.py
│
├── frontend
│   ├── src
│   │   ├── components
│   │   ├── pages
│   │   ├── api
│   │   ├── types
│   │   └── assets
│   └── package.json
│
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/jdpapena/saliksik.git
cd saliksik
```

---

## Backend Setup

```bash
cd backend

uv sync

uv run uvicorn app.main:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

## Environment Variables

Create a `.env` file inside the frontend directory.

```env
VITE_API_URL=http://127.0.0.1:8000
```

---

## Sample Workflow

```text
User enters ticker/symbol
        │
        ▼
React Frontend
        │
        ▼
FastAPI REST API
        │
        ▼
Yahoo Finance
        │
        ▼
Scoring Engine
        │
        ▼
Summary Generator
        │
        ▼
React Dashboard
```

---

## Example Analysis

### Overall Assessment

```
Overall Score : 84 / 100
Rating        : ★★★★☆
Assessment    : Good
```

### Categories

```
Financial Health : ★★★★★
Growth           : ★★★★☆
Valuation        : ★★☆☆☆
Risk             : ★★★★☆
Market Sentiment : ★★★☆☆
```

---

## Future Improvements
- Historical stock price charts
- Stock comparison dashboard
- Watchlist functionality
- Search history
- Latest financial news integration
- Portfolio tracking
- Philippine Stock Exchange support

---

## Disclaimer
SALIKSIK is intended for educational and research purposes only. It does not provide financial advice or investment recommendations. Users should conduct their own due diligence before making investment decisions.

---
