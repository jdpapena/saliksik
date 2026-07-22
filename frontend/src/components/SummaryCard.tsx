import type { StockAnalysis } from "../types/stock";

type Props = {
  analysis: StockAnalysis;
};

function SummaryCard({ analysis }: Props) {
  return (
    <div className="mt-6 rounded-xl bg-white p-6 shadow">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold">{analysis.company_name}</h2>

          <p className="text-gray-500">
            {analysis.ticker} • {analysis.sector}
          </p>
        </div>

        <span className="rounded-full bg-green-100 px-4 py-2 font-semibold text-green-700">
          {analysis.summary.assessment}
        </span>
      </div>

      <p className="mt-6 text-gray-700">{analysis.summary.overview}</p>
    </div>
  );
}

export default SummaryCard;
