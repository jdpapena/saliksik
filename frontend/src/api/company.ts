const API_BASE = "http://127.0.0.1:8000";

export async function compareCompanies(tickerA: string, tickerB: string) {
    const response = await fetch(
        `${API_BASE}/companies/compare/${tickerA}/${tickerB}`,
    );

    if (!response.ok) {
        throw new Error("Failed to compare companies.");
    }

    return response.json();
}

export interface CompanySearchResult {
    ticker: string;
    company_name: string;
    exchange: string | null;
    source: string;
}

export async function searchCompanies(
    query: string,
): Promise<CompanySearchResult[]> {
    const normalizedQuery = query.trim();

    if (!normalizedQuery) {
        return [];
    }

    const response = await fetch(
        `${API_BASE}/companies/search?query=${encodeURIComponent(
            normalizedQuery,
        )}`,
    );

    if (!response.ok) {
        throw new Error("Failed to search companies.");
    }

    return response.json();
}
