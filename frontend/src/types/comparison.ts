export interface MetricComparison {
    id: string;

    metric: string;

    definition: string;

    formula: string;

    why_it_matters: string;

    things_to_consider: string;

    company_a_value: string | null;

    company_b_value: string | null;

    unit: string;
}

export interface CompanyComparison {
    ticker_a: string;
    name_a: string;
    report_date_a: string;

    ticker_b: string;
    name_b: string;
    report_date_b: string;

    fiscal_year: number;

    metrics: MetricComparison[];
}
