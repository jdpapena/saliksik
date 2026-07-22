import { useState } from "react";
import { getStockAnalysis } from "./api/stock";

function App() {
  const [ticker, setTicker] = useState("");

  const searchStock = async () => {
    if (!ticker.trim()) {
      alert("Please enter a stock ticker.");
      return;
    }

    try {
      const data = await getStockAnalysis(ticker.toUpperCase());

      console.log(data);

      alert(`${data.company_name}\n${data.score.recommendation}`);
    } catch (error) {
      console.error(error);
      alert("Stock not found.");
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

      <main className="mx-auto max-w-7xl p-6">
        <div className="rounded-xl bg-white p-6 shadow">
          <h2 className="mb-4 text-2xl font-semibold">Search a Stock</h2>

          <input
            type="text"
            placeholder="Enter ticker (e.g. AAPL)"
            value={ticker}
            onChange={(e) => setTicker(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                searchStock();
              }
            }}
            className="w-full rounded-lg border border-gray-300 px-4 py-3 focus:border-blue-500 focus:outline-none"
          />
        </div>
      </main>
    </div>
  );
}

export default App;
