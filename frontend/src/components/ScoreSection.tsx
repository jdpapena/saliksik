import ScoreCard from "./ScoreCard";
import type { StockAnalysis } from "../types/stock";

type Props = {
  analysis: StockAnalysis;
};

function ScoreSection({ analysis }: Props) {
  return (
    <div className="mt-6 grid gap-4 md:grid-cols-2 lg:grid-cols-5">
      <ScoreCard
        title="Financial Health"
        stars={analysis.score.financial_health.stars}
        description={analysis.score.financial_health.explanation}
      />

      <ScoreCard
        title="Growth"
        stars={analysis.score.growth.stars}
        description={analysis.score.growth.explanation}
      />

      <ScoreCard
        title="Valuation"
        stars={analysis.score.valuation.stars}
        description={analysis.score.valuation.explanation}
      />

      <ScoreCard
        title="Risk"
        stars={analysis.score.risk.stars}
        description={analysis.score.risk.explanation}
      />

      <ScoreCard
        title="Market Sentiment"
        stars={analysis.score.market_sentiment.stars}
        description={analysis.score.market_sentiment.explanation}
      />
    </div>
  );
}

export default ScoreSection;
