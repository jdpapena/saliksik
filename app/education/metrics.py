"""
Stores one consistent explanation for every metric displayed by SALIKSIK.

Primary reference:
CFA Institute financial statement analysis materials.

The descriptions are rewritten in SALIKSIK's own beginner-friendly
language rather than copied directly from the reference.
"""


METRIC_DEFINITIONS: dict[str, dict[str, str]] = {
    "revenue": {
        "display_name": "Revenue",
        "definition": (
            "The amount earned from a company's main business "
            "activities during the reporting period."
        ),
        "formula": (
            "Reported from the income statement. It generally "
            "represents sales of products and services."
        ),
        "why_it_matters": (
            "Revenue shows the scale of the company's operations "
            "and helps users track whether sales changed over time."
        ),
        "things_to_consider": (
            "Compare revenue across several years and with companies "
            "that operate in similar industries. Revenue does not "
            "include the expenses required to generate those sales."
        ),
    },
    "gross_profit": {
        "display_name": "Gross Profit",
        "definition": (
            "Revenue remaining after subtracting the direct costs "
            "of producing the goods or services sold."
        ),
        "formula": "Revenue - Cost of revenue",
        "why_it_matters": (
            "Gross profit helps show how much remains from sales "
            "before operating, financing, and tax expenses."
        ),
        "things_to_consider": (
            "Cost structures differ between industries, so comparisons "
            "are usually more meaningful between similar businesses."
        ),
    },
    "operating_income": {
        "display_name": "Operating Income",
        "definition": (
            "Profit generated from the company's main operations "
            "before interest and income taxes."
        ),
        "formula": (
            "Gross profit - Operating expenses"
        ),
        "why_it_matters": (
            "It helps users examine the earnings produced by the "
            "company's core business activities."
        ),
        "things_to_consider": (
            "Companies may classify certain operating costs differently. "
            "Reviewing several reporting periods provides more context."
        ),
    },
    "net_income": {
        "display_name": "Net Income",
        "definition": (
            "Profit remaining after operating costs, interest, taxes, "
            "and other recognized gains or losses."
        ),
        "formula": "Total income - Total recognized expenses",
        "why_it_matters": (
            "Net income shows how much accounting profit the company "
            "reported for the period."
        ),
        "things_to_consider": (
            "Net income can be affected by one-time items and accounting "
            "estimates, so it can be reviewed together with cash flow."
        ),
    },
    "earnings_per_share": {
        "display_name": "Diluted Earnings per Share",
        "definition": (
            "The portion of earnings attributable to each common share "
            "after accounting for potentially dilutive securities."
        ),
        "formula": (
            "Earnings available to common shareholders / "
            "Diluted weighted-average shares"
        ),
        "why_it_matters": (
            "EPS allows earnings to be viewed on a per-share basis and "
            "compared across reporting periods."
        ),
        "things_to_consider": (
            "Share repurchases, new share issuance, stock splits, and "
            "dilutive securities can change EPS independently of profit."
        ),
    },
    "cash_and_equivalents": {
        "display_name": "Cash and Cash Equivalents",
        "definition": (
            "Cash and short-term highly liquid investments available "
            "to the company at the reporting date."
        ),
        "formula": "Reported directly on the balance sheet",
        "why_it_matters": (
            "It shows resources that may be available for near-term "
            "payments, operations, investment, or financing needs."
        ),
        "things_to_consider": (
            "Cash should be viewed together with liabilities, operating "
            "needs, debt obligations, and planned investments."
        ),
    },
    "current_assets": {
        "display_name": "Current Assets",
        "definition": (
            "Assets expected to be converted into cash, sold, or used "
            "within the company's normal operating cycle."
        ),
        "formula": "Reported directly on the balance sheet",
        "why_it_matters": (
            "Current assets help users examine the resources available "
            "for short-term operations and obligations."
        ),
        "things_to_consider": (
            "Current assets can include inventory and receivables, which "
            "may not be converted into cash immediately."
        ),
    },
    "total_assets": {
        "display_name": "Total Assets",
        "definition": (
            "The total reported value of resources controlled by the "
            "company at the reporting date."
        ),
        "formula": "Liabilities + Shareholders' equity",
        "why_it_matters": (
            "Total assets provides context about the size and resource "
            "base of a company."
        ),
        "things_to_consider": (
            "Asset composition differs between industries, and reported "
            "book values may differ from current market values."
        ),
    },
    "current_liabilities": {
        "display_name": "Current Liabilities",
        "definition": (
            "Obligations expected to be settled within the company's "
            "normal operating cycle or within approximately one year."
        ),
        "formula": "Reported directly on the balance sheet",
        "why_it_matters": (
            "Current liabilities show the amount of obligations the "
            "company expects to address in the near term."
        ),
        "things_to_consider": (
            "Review them together with current assets and operating cash "
            "flows rather than interpreting the amount by itself."
        ),
    },
    "total_liabilities": {
        "display_name": "Total Liabilities",
        "definition": (
            "The company's total reported obligations to lenders, "
            "suppliers, employees, governments, and other parties."
        ),
        "formula": "Total assets - Shareholders' equity",
        "why_it_matters": (
            "Total liabilities helps users understand how much of the "
            "company's assets are financed through obligations."
        ),
        "things_to_consider": (
            "Liabilities include more than interest-bearing debt. Their "
            "terms, timing, and purpose should also be considered."
        ),
    },
    "shareholders_equity": {
        "display_name": "Shareholders' Equity",
        "definition": (
            "The residual accounting interest in the company's assets "
            "after subtracting liabilities."
        ),
        "formula": "Total assets - Total liabilities",
        "why_it_matters": (
            "Equity shows the reported net asset amount attributable "
            "to shareholders."
        ),
        "things_to_consider": (
            "Book equity may differ substantially from market value and "
            "can be affected by dividends, profits, losses, and buybacks."
        ),
    },
    "operating_cash_flow": {
        "display_name": "Operating Cash Flow",
        "definition": (
            "Net cash generated or used by the company's main operating "
            "activities during the reporting period."
        ),
        "formula": (
            "Operating cash receipts - Operating cash payments, "
            "with applicable cash-flow adjustments"
        ),
        "why_it_matters": (
            "It helps users examine whether business operations produced "
            "cash during the period."
        ),
        "things_to_consider": (
            "Working-capital movements and payment timing can cause "
            "operating cash flow to vary between periods."
        ),
    },
    "capital_expenditure": {
        "display_name": "Capital Expenditure",
        "definition": (
            "Cash spent to acquire or improve long-term property, plant, "
            "equipment, and similar productive assets."
        ),
        "formula": (
            "Reported as purchases of property, plant, and equipment "
            "in the investing section of the cash-flow statement"
        ),
        "why_it_matters": (
            "Capital expenditure shows how much cash the company used "
            "for long-term operating assets."
        ),
        "things_to_consider": (
            "Spending requirements vary greatly by industry, and capital "
            "expenditure may support maintenance, expansion, or both."
        ),
    },
}

METRIC_SOURCE = {
    "organization": "CFA Institute",
    "reference_area": "Financial Statement Analysis",
    "accessed_date": "2026-08-02",
}