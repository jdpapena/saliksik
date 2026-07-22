import type { StockAnalysis } from "../types/stock";

type Props = {
  analysis: StockAnalysis;
};

function StrengthWeaknessCard({ analysis }: Props) {
  return (
    <div className="mt-6 grid gap-6 md:grid-cols-2">
      <div className="rounded-xl bg-white p-6 shadow">
        <h2 className="mb-4 text-xl font-semibold text-green-700">Strengths</h2>

        <ul className="space-y-3">
          {analysis.summary.strengths.map((item: string) => (
            <li key={item} className="flex items-start gap-2">
              <span className="text-green-600">✓</span>
              <span>{item}</span>
            </li>
          ))}
        </ul>
      </div>

      <div className="rounded-xl bg-white p-6 shadow">
        <h2 className="mb-4 text-xl font-semibold text-red-700">Weaknesses</h2>

        <ul className="space-y-3">
          {analysis.summary.weaknesses.map((item: string) => (
            <li key={item} className="flex items-start gap-2">
              <span className="text-red-600">•</span>
              <span>{item}</span>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default StrengthWeaknessCard;
