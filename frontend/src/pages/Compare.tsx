import { useState } from "react";

import { compareCompanies } from "../api/company";
import CompanyHeader from "@/components/CompanyHeader";
import CompareForm from "../components/CompareForm";
import MetricCard from "../components/MetricCard";
import ComparisonSkeleton from "@/components/ComparisonSkeleton";
import type { CompanyComparison } from "../types/comparison";

export default function Compare() {
    const [comparison, setComparison] = useState<CompanyComparison | null>(
        null,
    );
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    async function handleCompare(tickerA: string, tickerB: string) {
        setLoading(true);
        setError(null);
        setComparison(null);

        try {
            const result = await compareCompanies(tickerA, tickerB);

            setComparison(result);
        } catch {
            setComparison(null);
            setError(
                "Unable to compare these companies. Confirm that both companies and their financial records have been synchronized.",
            );
        } finally {
            setLoading(false);
        }
    }

    return (
        <main className="min-h-screen bg-[oklch(0.95_0.015_78)] text-foreground">
            <section className="border-b bg-[oklch(0.91_0.03_72)]">
                <div className="mx-auto max-w-6xl px-4 py-12 text-center sm:px-6 sm:py-16">
                    <p className="mb-3 text-sm font-semibold tracking-[0.25em] text-primary">
                        SALIKSIK
                    </p>

                    <h1 className="text-4xl font-bold tracking-tight sm:text-5xl">
                        Compare companies using reported facts
                    </h1>

                    <p className="mx-auto mt-5 max-w-2xl text-muted-foreground">
                        Review financial information side by side without
                        scores, rankings, or investment recommendations.
                    </p>
                </div>
            </section>

            <section className="mx-auto max-w-6xl space-y-8 px-4 py-8 sm:px-6 sm:py-10">
                <CompareForm onCompare={handleCompare} loading={loading} />

                {error && (
                    <div className="rounded-lg border border-destructive/30 bg-destructive/10 px-4 py-3 text-sm text-destructive">
                        {error}
                    </div>
                )}

                {loading && <ComparisonSkeleton />}

                {comparison && !loading && (
                    <>
                        <div className="grid gap-6 md:grid-cols-2">
                            <CompanyHeader
                                ticker={comparison.ticker_a}
                                name={comparison.name_a}
                                reportDate={comparison.report_date_a}
                            />

                            <CompanyHeader
                                ticker={comparison.ticker_b}
                                name={comparison.name_b}
                                reportDate={comparison.report_date_b}
                            />
                        </div>

                        <div className="flex flex-col gap-3 border-b pb-5 sm:flex-row sm:items-end sm:justify-between">
                            <div>
                                <p className="text-sm font-medium text-primary">
                                    Financial comparison
                                </p>

                                <h2 className="mt-1 text-2xl font-semibold">
                                    Reported company metrics
                                </h2>
                            </div>

                            <p className="max-w-md text-sm text-muted-foreground">
                                Values may cover different report dates. Review
                                the dates shown above.
                            </p>
                        </div>

                        <div className="grid gap-4">
                            {comparison.metrics.map((metric) => (
                                <MetricCard
                                    key={metric.id}
                                    metric={metric}
                                    companyAName={comparison.ticker_a}
                                    companyBName={comparison.ticker_b}
                                />
                            ))}
                        </div>
                    </>
                )}
            </section>
        </main>
    );
}
