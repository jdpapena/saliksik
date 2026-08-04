# SALIKSIK - Financial Research Platform
![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-green)
![React](https://img.shields.io/badge/React-19-blue)
![TypeScript](https://img.shields.io/badge/TypeScript-5-blue)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A full-stack financial research platform engineered to help beginner investors discover and compare publicly traded companies using reported SEC financial data. The application automatically synchronizes company information, annual financial statements, and presents side-by-side comparisons without relying on subjective scores or investment recommendations.

This project was built to practice full-stack software engineering by integrating external financial data sources, designing a layered backend architecture, and developing a responsive frontend that simplifies company research for new investors.

---

## Features

- **Automatic Company Synchronization:** Downloads and stores company information directly from the SEC EDGAR database when requested.
- **Automatic Financial Synchronization:** Retrieves annual reported financial facts and caches them locally for faster future access.
- **Company Directory Search:** Searches more than 10,000 SEC-listed companies with real-time autocomplete.
- **Side-by-Side Financial Comparison:** Displays reported financial metrics for two companies using the latest available fiscal year.
- **Educational Metric Explanations:** Explains financial definitions, formulas, and why each metric matters to beginner investors.
- **Local Data Caching:** Previously synchronized companies are stored locally to reduce unnecessary API requests and improve performance.

---

## Technologies

- **Backend:** Python, FastAPI, SQLAlchemy ORM, SQLite (Development), PostgreSQL Ready, Pydantic, HTTPX
- **Frontend:** React, TypeScript, Vite, Tailwind CSS, shadcn/ui
- **External Data:** SEC EDGAR Company Facts API, SEC Company Directory

---

## How it works

The application processes company data in five steps:

1. **Searches the SEC Directory:** Looks up companies from a locally cached SEC directory containing more than 10,000 publicly traded companies.
2. **Synchronizes Company Information:** Downloads company metadata from SEC EDGAR if it has not been synchronized previously.
3. **Synchronizes Financial Statements:** Retrieves annual reported financial facts and stores them locally for future requests.
4. **Processes Financial Metrics:** Extracts standardized financial metrics and aligns both companies using a shared fiscal year.
5. **Displays Comparison:** Presents reported financial values together with educational explanations for each metric.

---

## Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/jdpapena/saliksik.git
cd saliksik
```

### 2. Install Backend Dependencies

```bash
uv sync
```

### 3. Configure Environment Variables

Create a `.env` file in the project root.

```env
DATABASE_URL=sqlite:///./saliksik.db
SEC_USER_AGENT=SALIKSIK your-email@example.com
FRONTEND_URL=http://localhost:5173
```

### 4. Start the Backend

```bash
uv run uvicorn app.main:app --reload
```

### 5. Start the Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## Sample Workflow

```
User enters:

AAPL
MSFT

↓

Company Directory Search

↓

Automatic SEC Synchronization

↓

Financial Synchronization

↓

Metric Processing

↓

Side-by-Side Comparison
```

---

## Project Structure

```
saliksik/
│
├── app/
│   ├── database/
│   ├── models/
│   ├── providers/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── tests/
├── start.sh
├── pyproject.toml
└── README.md
```

---

## Future Improvements

Version 2 of SALIKSIK is planned to include: (coming soon)

- Investor profile questionnaire
- Personalized company recommendations
- Growth vs. dividend preference analysis
- Long-term vs. short-term investing goals
- AI-powered financial assistant
- Philippine Stock Exchange support
- Portfolio tracking

---

## Disclaimer

SALIKSIK is an educational and personal portfolio project developed to demonstrate full-stack software engineering, financial data integration, and application design.

The information presented is derived from publicly available SEC filings and is intended solely for research and educational purposes.

This application:

- Does **not** provide financial, investment, legal, or tax advice.
- Does **not** recommend buying, selling, or holding any security.
- Should **not** be used as the sole basis for making investment decisions.
- Is intended for **personal and non-commercial use**.

Users are encouraged to conduct their own research and consult a qualified financial professional before making investment decisions.

---
