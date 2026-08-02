import { Badge } from "@/components/ui/badge";
import {
    Card,
    CardDescription,
    CardHeader,
    CardTitle,
} from "@/components/ui/card";

interface CompanyHeaderProps {
    ticker: string;
    name: string;
    reportDate: string;
}

function formatDate(value: string): string {
    return new Intl.DateTimeFormat("en-US", {
        year: "numeric",
        month: "short",
        day: "numeric",
    }).format(new Date(`${value}T00:00:00`));
}

export default function CompanyHeader({
    ticker,
    name,
    reportDate,
}: CompanyHeaderProps) {
    return (
        <Card className="w-full">
            <CardHeader className="space-y-4">
                <div className="flex items-center justify-between gap-4">
                    <Badge variant="secondary">{ticker}</Badge>

                    <span className="text-xs text-muted-foreground">
                        Latest annual report
                    </span>
                </div>

                <div>
                    <CardTitle className="text-2xl">{name}</CardTitle>

                    <CardDescription className="mt-2">
                        Report date: {formatDate(reportDate)}
                    </CardDescription>
                </div>
            </CardHeader>
        </Card>
    );
}
