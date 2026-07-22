type Props = {
  title: string;
  value: string | number;
};

function MetricsCard({ title, value }: Props) {
  return (
    <div className="rounded-xl bg-white p-5 shadow">
      <p className="text-sm text-gray-500">{title}</p>

      <h3 className="mt-2 text-2xl font-bold">{value ?? "N/A"}</h3>
    </div>
  );
}

export default MetricsCard;
