export type ScoreCategory = {
  score: number;
  max_score: number;
  stars: number;
  explanation: string;
};

export type Score = {
  financial_health: ScoreCategory;
  growth: ScoreCategory;
  valuation: ScoreCategory;
  risk: ScoreCategory;
  market_sentiment: ScoreCategory;
  overall: number;
  overall_stars: number;
  grade: string;
  assessment: string;
  strengths: string[];
  weaknesses: string[];
};

export type StockSummary = {
  ticker: string;
  assessment: string;
  strengths: string[];
  weaknesses: string[];
  overview: string;
};

export type StockAnalysis = {
  ticker: string;
  company_name: string;
  sector: string | null;
  industry: string | null;
  country: string | null;
  market_cap: number | null;
  score: Score;
  summary: StockSummary;
};