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
