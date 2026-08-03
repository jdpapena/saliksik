import { useEffect, useState } from "react";

import { searchCompanies, type CompanySearchResult } from "@/api/company";
import { Input } from "@/components/ui/input";

interface CompanyAutocompleteProps {
    id: string;
    label: string;
    value: string;
    placeholder?: string;
    onChange: (value: string) => void;
}

export default function CompanyAutocomplete({
    id,
    label,
    value,
    placeholder,
    onChange,
}: CompanyAutocompleteProps) {
    const [results, setResults] = useState<CompanySearchResult[]>([]);
    const [open, setOpen] = useState(false);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        const query = value.trim();

        if (query.length < 2) {
            setResults([]);
            setOpen(false);
            return;
        }

        const timeoutId = window.setTimeout(async () => {
            setLoading(true);

            try {
                const companies = await searchCompanies(query);

                setResults(companies);
                setOpen(true);
            } catch {
                setResults([]);
                setOpen(false);
            } finally {
                setLoading(false);
            }
        }, 250);

        return () => window.clearTimeout(timeoutId);
    }, [value]);

    function selectCompany(company: CompanySearchResult) {
        onChange(company.ticker);
        setOpen(false);
    }

    return (
        <div className="relative space-y-2">
            <label className="text-sm font-medium" htmlFor={id}>
                {label}
            </label>

            <Input
                id={id}
                value={value}
                onChange={(event) => {
                    onChange(event.target.value);
                    setOpen(true);
                }}
                onFocus={() => {
                    if (results.length > 0) {
                        setOpen(true);
                    }
                }}
                placeholder={placeholder}
                autoComplete="off"
            />

            {open && (
                <div className="absolute z-50 mt-1 w-full overflow-hidden rounded-md border bg-popover text-popover-foreground shadow-md">
                    {loading && (
                        <p className="px-3 py-3 text-sm text-muted-foreground">
                            Searching…
                        </p>
                    )}

                    {!loading && results.length === 0 && (
                        <p className="px-3 py-3 text-sm text-muted-foreground">
                            No cached companies found.
                        </p>
                    )}

                    {!loading &&
                        results.map((company) => (
                            <button
                                key={company.ticker}
                                type="button"
                                className="flex w-full items-start justify-between gap-3 px-3 py-3 text-left hover:bg-accent"
                                onMouseDown={(event) => event.preventDefault()}
                                onClick={() => selectCompany(company)}
                            >
                                <span>
                                    <span className="block font-medium">
                                        {company.company_name}
                                    </span>

                                    <span className="block text-xs text-muted-foreground">
                                        {company.exchange}
                                    </span>
                                </span>

                                <span className="text-right">
                                    <span className="block text-sm font-semibold">
                                        {company.ticker}
                                    </span>

                                    <span className="block text-xs text-muted-foreground">
                                        {company.source}
                                    </span>
                                </span>
                            </button>
                        ))}
                </div>
            )}
        </div>
    );
}
