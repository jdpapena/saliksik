import { Card, CardContent, CardHeader } from "@/components/ui/card";
import { Skeleton } from "@/components/ui/skeleton";

export default function ComparisonSkeleton() {
    return (
        <div className="space-y-8">
            <div className="grid gap-6 md:grid-cols-2">
                {[0, 1].map((item) => (
                    <Card key={item}>
                        <CardHeader className="space-y-4">
                            <Skeleton className="h-6 w-20" />
                            <Skeleton className="h-8 w-3/4" />
                            <Skeleton className="h-4 w-1/2" />
                        </CardHeader>
                    </Card>
                ))}
            </div>

            <div className="space-y-4">
                {[0, 1, 2].map((item) => (
                    <Card key={item}>
                        <CardHeader>
                            <Skeleton className="h-6 w-40" />
                        </CardHeader>

                        <CardContent className="space-y-5">
                            <div className="space-y-3">
                                <Skeleton className="h-5 w-full" />
                                <Skeleton className="h-3 w-full rounded-full" />
                            </div>

                            <div className="space-y-3">
                                <Skeleton className="h-5 w-full" />
                                <Skeleton className="h-3 w-3/4 rounded-full" />
                            </div>
                        </CardContent>
                    </Card>
                ))}
            </div>
        </div>
    );
}
