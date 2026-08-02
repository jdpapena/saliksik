import { useState } from "react";

import { Button } from "@/components/ui/button";
import {
    Card,
    CardContent,
    CardDescription,
    CardHeader,
    CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Separator } from "@/components/ui/separator";

interface CompareFormProps {
    onCompare: (tickerA: string, tickerB: string) => void;
    loading?: boolean;
}

export default function CompareForm({
    onCompare,
    loading = false,
}: CompareFormProps) {
    const [tickerA, setTickerA] = useState("AAPL");
    const [tickerB, setTickerB] = useState("MSFT");

    function handleCompare() {
        const firstTicker = tickerA.trim().toUpperCase();
        const secondTicker = tickerB.trim().toUpperCase();

        if (!firstTicker || !secondTicker) {
            return;
        }

        onCompare(firstTicker, secondTicker);
    }

    return (
        <Card>
            <CardHeader>
                <CardTitle>Choose two companies</CardTitle>

                <CardDescription>
                    Enter two US stock tickers with synchronized SEC financial
                    data.
                </CardDescription>
            </CardHeader>

            <CardContent className="space-y-6">
                <div className="grid gap-4 md:grid-cols-[1fr_auto_1fr] md:items-end">
                    <div className="space-y-2">
                        <label
                            className="text-sm font-medium"
                            htmlFor="ticker-a"
                        >
                            First company
                        </label>

                        <Input
                            id="ticker-a"
                            value={tickerA}
                            onChange={(event) =>
                                setTickerA(event.target.value.toUpperCase())
                            }
                            placeholder="AAPL"
                            maxLength={10}
                            autoComplete="off"
                        />
                    </div>

                    <div className="hidden items-center justify-center pb-2 md:flex">
                        <span className="rounded-full border bg-muted px-3 py-1 text-xs font-semibold text-muted-foreground">
                            VS
                        </span>
                    </div>

                    <div className="space-y-2">
                        <label
                            className="text-sm font-medium"
                            htmlFor="ticker-b"
                        >
                            Second company
                        </label>

                        <Input
                            id="ticker-b"
                            value={tickerB}
                            onChange={(event) =>
                                setTickerB(event.target.value.toUpperCase())
                            }
                            placeholder="MSFT"
                            maxLength={10}
                            autoComplete="off"
                        />
                    </div>
                </div>

                <Separator />

                <div className="flex justify-end">
                    <Button
                        type="button"
                        onClick={handleCompare}
                        disabled={loading}
                    >
                        {loading
                            ? "Comparing companies..."
                            : "Compare companies"}
                    </Button>
                </div>
            </CardContent>
        </Card>
    );
}
