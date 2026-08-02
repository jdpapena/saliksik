import {
    Accordion,
    AccordionContent,
    AccordionItem,
    AccordionTrigger,
} from "@/components/ui/accordion";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

import type { MetricComparison } from "../types/comparison";

interface MetricCardProps {
    metric: MetricComparison;
    companyAName: string;
    companyBName: string;
}

function formatValue(value: string | null, unit: string): string {
    if (value === null) {
        return "Not available";
    }

    const number = Number(value);

    if (unit === "USD/share") {
        return `$${number.toFixed(2)} per share`;
    }

    if (unit === "USD") {
        if (Math.abs(number) >= 1_000_000_000) {
            return `$${(number / 1_000_000_000).toFixed(2)}B`;
        }

        if (Math.abs(number) >= 1_000_000) {
            return `$${(number / 1_000_000).toFixed(2)}M`;
        }

        return `$${number.toLocaleString()}`;
    }

    return `${number.toLocaleString()} ${unit}`;
}

export default function MetricCard({
    metric,
    companyAName,
    companyBName,
}: MetricCardProps) {
    return (
        <Card>
            <CardHeader className="flex flex-row items-center justify-between gap-4">
                <CardTitle className="text-lg">{metric.metric}</CardTitle>

                <Badge variant="outline">{metric.unit}</Badge>
            </CardHeader>

            <CardContent className="space-y-5">
                <div className="grid gap-3 sm:grid-cols-2">
                    <div className="rounded-lg border bg-muted/30 p-4">
                        <p className="text-sm font-medium text-muted-foreground">
                            {companyAName}
                        </p>

                        <p className="mt-2 text-2xl font-semibold tracking-tight">
                            {formatValue(metric.company_a_value, metric.unit)}
                        </p>
                    </div>

                    <div className="rounded-lg border bg-muted/30 p-4">
                        <p className="text-sm font-medium text-muted-foreground">
                            {companyBName}
                        </p>

                        <p className="mt-2 text-2xl font-semibold tracking-tight">
                            {formatValue(metric.company_b_value, metric.unit)}
                        </p>
                    </div>
                </div>

                <Accordion type="single" collapsible>
                    <AccordionItem value={metric.id}>
                        <AccordionTrigger>
                            Learn about this metric
                        </AccordionTrigger>

                        <AccordionContent>
                            <div className="grid gap-5 pt-2 sm:grid-cols-2">
                                <section>
                                    <h4 className="text-sm font-semibold">
                                        Definition
                                    </h4>

                                    <p className="mt-2 text-sm leading-6 text-muted-foreground">
                                        {metric.definition}
                                    </p>
                                </section>

                                <section>
                                    <h4 className="text-sm font-semibold">
                                        Formula
                                    </h4>

                                    <p className="mt-2 text-sm leading-6 text-muted-foreground">
                                        {metric.formula}
                                    </p>
                                </section>

                                <section>
                                    <h4 className="text-sm font-semibold">
                                        Why it matters
                                    </h4>

                                    <p className="mt-2 text-sm leading-6 text-muted-foreground">
                                        {metric.why_it_matters}
                                    </p>
                                </section>

                                <section>
                                    <h4 className="text-sm font-semibold">
                                        Things to consider
                                    </h4>

                                    <p className="mt-2 text-sm leading-6 text-muted-foreground">
                                        {metric.things_to_consider}
                                    </p>
                                </section>
                            </div>
                        </AccordionContent>
                    </AccordionItem>
                </Accordion>
            </CardContent>
        </Card>
    );
}
