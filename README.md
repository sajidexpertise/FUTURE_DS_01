# Northstar | Business Sales Performance Analytics

**Future Interns · Data Science & Analytics · Task 1**  
**Repository name:** `FUTURE_DS_01`  
**Author:** Sajid Ali

**Northstar** is an interactive, offline sales dashboard for **Northline Goods**, a fictional home and lifestyle retailer. It uses a dark, desktop-first analytical layout with responsive mobile panels. This case study examines 2024–2025 net sales, gross profit, product and category performance, regional mix, and returns. The records are **synthetic demonstration data**, generated for this project; they do not describe a real business or real customers.

## Open the dashboard

Download this project and double-click **`index.html`**. No server, installation, login or internet connection is required. Select a year, region, category or channel to update every KPI, chart and action card. Click a regional rank to filter it, use **Reset** to return to 2025, or **Export CSV** to download the selected records. The left navigation jumps to the corresponding analysis panels. The desktop chart grid stacks vertically on narrow screens.

To publish: create a public GitHub repository named **`FUTURE_DS_01`**, upload the *contents* of this folder to its root, and enable GitHub Pages from the `main` branch root. The address will be `https://sajidexpertise.github.io/FUTURE_DS_01/` if the repository belongs to that account. Verify the URL after publishing.

## Executive findings

For 2025, recognized net sales were **$225,031.45**, up **23.2%** from 2024; gross profit was **$102,404.45**, up **22.6%**. Gross margin was **45.5%**, approximately **0.24 percentage points lower** than 2024. North led regional sales at **$70,145.85**, closely followed by East at **$68,377.05**. Home Office led categories at **$67,499.60**, and the Ergonomic Chair led individual products at **$35,206.50**. Marketplace had the highest 2025 return rate, **25 of 335 orders (7.46%)**.

### Actions for a business stakeholder

1. **Protect capacity in North and investigate East's growth.** East sales grew approximately 43.5% year over year, substantially faster than North's approximately 18.0%. Compare stock availability and delivery times before shifting inventory or spending.
2. **Review Home Office product economics.** It leads revenue, but its approximately 44.2% gross margin trails Everyday's approximately 50.2%. Check item costs, discount policy and product mix before increasing promotion.
3. **Audit Marketplace returns.** Its 7.46% return rate exceeds Online's 4.72% and Retail's 3.01%. Gather return reasons and review listings and fulfillment; these records alone do not establish why returns occurred.

See [the analysis report](docs/ANALYSIS.md) for definitions, supporting calculations, interpretation and limitations.

## Project files

| File | Purpose |
| --- | --- |
| `index.html` | Ready-to-open offline interactive dashboard, with data embedded |
| `dashboard.template.html` | Editable dashboard source; generated file contains the dataset |
| `data/orders.csv` | 3,729 synthetic order records across 2024–2025 |
| `data/summary.json` | Independently generated yearly and segment summaries |
| `scripts/build.py` | Deterministic generator and build script, Python standard library only |
| `docs/ANALYSIS.md` | Client-facing analysis and recommended next steps |

## Rebuild

From inside the repository: `python scripts/build.py` (on Windows, `py scripts\build.py` also works). The script regenerates `orders.csv`, `summary.json` and `index.html` from the fixed seed and documented assumptions. Commit all three generated outputs to GitHub so GitHub Pages can serve the dashboard directly.

## Metric definitions and scope

- One row is one order with one product line, and `order_id` is unique. `units` is the quantity for that line. There are no customer identities, shipping fees, tax records, advertising costs or operational expenses.
- `returned=True` means a fully returned order. The row remains in the export and in return-rate denominators, but contributes **zero** to recognized net sales, cost of goods and gross profit. This is a simplified case-study accounting convention.
- Net sales on a completed order = `units × unit_price_usd × (1 − discount_rate)`.
- Gross profit = net sales − cost of goods sold. Gross margin = gross profit / net sales. This is **gross**, not net business profit.
- Completed orders exclude fully returned orders. Average order value = net sales / completed orders. Return rate = returned order rows / all order rows.
- Year-over-year comparisons use the same filter selections applied to 2024 and 2025. When viewing both years, comparison percentages are suppressed.
- The line chart compares full calendar months. The current dataset covers all months in both years, so 2025 vs 2024 is a like-for-like comparison.

## Data provenance and integrity

No real sales data was supplied with the task brief. `scripts/build.py` constructs sample transactions with seasonal order volumes, a product catalog, regional and channel mix, discounts and returns. The dashboard computes filtered measures from the embedded source rows in your browser; the yearly `summary.json` is produced separately in Python for reconciliation. Findings apply to **this simulated scenario only**. Before applying them to an actual client, replace the sample records, reconcile returns and discounts to the client's accounting rules, and review return reasons and unit economics.

## Internship submission

Use the exact public repository name **`FUTURE_DS_01`**, as required for the DS track. Submit the repository through the official Future Interns task submission portal during the dates on your offer letter, using your CIN ID. A GitHub Pages demo can supplement the repository, but it does not replace the portal submission.
