import type { StockAnalysis } from "../types/stock";

type Props = {
  analysis: StockAnalysis;
};

function formatMarketCap(value: number | null): string {
  if (value === null) return "N/A";

  if (value >= 1_000_000_000_000) {
    return `$${(value / 1_000_000_000_000).toFixed(2)}T`;
  }

  if (value >= 1_000_000_000) {
    return `$${(value / 1_000_000_000).toFixed(2)}B`;
  }

  if (value >= 1_000_000) {
    return `$${(value / 1_000_000).toFixed(2)}M`;
  }

  return `$${value.toLocaleString()}`;
}

function CompanySnapshot({ analysis }: Props) {
  return (
    <div className="mt-6 rounded-xl bg-white p-6 shadow">
      <h2 className="mb-6 text-2xl font-semibold">Company Snapshot</h2>

      <div className="grid grid-cols-2 gap-6">
        <div>
          <p className="text-sm text-gray-500">Ticker</p>
          <p className="font-semibold">{analysis.ticker}</p>
        </div>

        <div>
          <p className="text-sm text-gray-500">Sector</p>
          <p className="font-semibold">{analysis.sector ?? "N/A"}</p>
        </div>

        <div>
          <p className="text-sm text-gray-500">Industry</p>
          <p className="font-semibold">{analysis.industry ?? "N/A"}</p>
        </div>

        <div>
          <p className="text-sm text-gray-500">Country</p>
          <p className="font-semibold">{analysis.country ?? "N/A"}</p>
        </div>

        <div>
          <p className="text-sm text-gray-500">Market Capitalization</p>
          <p className="font-semibold">
            {formatMarketCap(analysis.market_cap)}
          </p>
        </div>
      </div>
    </div>
  );
}

export default CompanySnapshot;
