type ScoreCardProps = {
  title: string;
  stars: number;
  description: string;
};

function ScoreCard({ title, stars, description }: ScoreCardProps) {
  return (
    <div className="rounded-xl bg-white p-5 shadow">
      <h3 className="text-lg font-semibold">{title}</h3>

      <div className="mt-2 text-yellow-500 text-xl">
        {"★".repeat(stars)}
        {"☆".repeat(5 - stars)}
      </div>

      <p className="mt-3 text-sm text-gray-600">{description}</p>
    </div>
  );
}

export default ScoreCard;
