import axios from "axios";
import { useState } from "react";
import { getStockAnalysis } from "../api/stock";
import type { StockAnalysis } from "../types/stock";
import SummaryCard from "../components/SummaryCard";
import ScoreSection from "../components/ScoreSection";
import StrengthWeaknessCard from "../components/StrengthWeaknessCard";
import CompanySnapshot from "../components/CompanySnapshot";

function Home() {
  const [ticker, setTicker] = useState("");
  const [analysis, setAnalysis] = useState<StockAnalysis | null>(null);

  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  const searchStock = async () => {
    const cleanTicker = ticker.trim().toUpperCase();
    if (!cleanTicker) {
      setError("Please enter a stock ticker.");
      return;
    }

    try {
      setIsLoading(true);
      setError("");
      setAnalysis(null);

      const data = await getStockAnalysis(cleanTicker);

      setAnalysis(data);
    } catch (error) {
      console.error(error);

      if (axios.isAxiosError(error)) {
        if (error.response?.status === 404) {
          setError(
            "We couldn't find that stock ticker. Please check the symbol and try again.",
          );
        } else if (error.response?.status === 500) {
          setError(
            "Something went wrong on the server. Please try again later.",
          );
        } else if (!error.response) {
          setError(
            "Unable to connect to the server. Please check your internet connection.",
          );
        } else {
          setError("An unexpected error occurred.");
        }
      } else {
        setError("An unexpected error occurred.");
      }
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-100">
      <header className="bg-blue-700 text-white shadow">
        <div className="mx-auto max-w-7xl px-6 py-4">
          <h1 className="text-3xl font-bold">SALIKSIK</h1>
          <p className="text-blue-100">
            Simple stock analysis for beginner investors
          </p>
        </div>
      </header>

      <main className="mx-auto max-w-5xl p-6">
        <div className="rounded-xl bg-white p-6 shadow">
          <h2 className="mb-4 text-2xl font-semibold">Search a Stock</h2>
          <input
            type="text"
            placeholder="Enter ticker (e.g. AAPL)"
            value={ticker}
            disabled={isLoading}
            onChange={(e) => setTicker(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter" && !isLoading) {
                searchStock();
              }
            }}
            className="w-full rounded-lg border border-gray-300 px-4 py-3 focus:border-blue-500 focus:outline-none disabled:cursor-not-allowed disabled:bg-gray-100"
          />
          {isLoading && (
            <p className="mt-4 text-sm font-medium text-blue-700">
              Analyzing {ticker.trim().toUpperCase()}...
            </p>
          )}

          {error && (
            <div className="mt-4 rounded-lg bg-red-50 px-4 py-3 text-sm text-red-700">
              {error}
            </div>
          )}
        </div>
        {analysis && (
          <>
            <SummaryCard analysis={analysis} />
            <ScoreSection analysis={analysis} />
            <StrengthWeaknessCard analysis={analysis} />
            <CompanySnapshot analysis={analysis} />
          </>
        )}
      </main>
    </div>
  );
}

export default Home;
