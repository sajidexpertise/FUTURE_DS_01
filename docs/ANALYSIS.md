# Sales performance | Stakeholder report

**Northline Goods · fictional retailer · USD · full years 2024 and 2025**  
**Prepared by Sajid Ali | Future Interns Task 1**

## Decision summary

Net sales grew in 2025, while gross margin slipped slightly. North still generated the most revenue, although East is close behind and grew much faster. Home Office was the largest category by sales. The marketplace channel had the highest return incidence. These results support targeted reviews of inventory, category economics and return reasons; they are not evidence of causation.

| Measure | 2024 | 2025 | Change |
| --- | ---: | ---: | ---: |
| Net sales | $182,601.90 | $225,031.45 | +23.24% |
| Gross profit | $83,529.90 | $102,404.45 | +22.60% |
| Gross margin | 45.74% | 45.51% | −0.24 percentage points |
| Completed orders | 1,626 | 1,928 | +18.57% |
| Average order value | $112.30 | $116.72 | +3.94% |
| Fully returned orders | 83 / 1,709 | 92 / 2,020 | 4.86% → 4.55% |

Displayed percentage changes are calculated from unrounded values; the dashboard rounds some figures for display.

## Revenue pattern

October–December 2025 produced **$79,298.00**, or **35.2%** of annual net sales. This is consistent with the seasonal demand assumptions built into the simulation. Plan purchasing and staffing around the higher-volume period, then validate this pattern using actual history before acting.

## Regions and products

| 2025 region | Net sales | Share of 2025 sales | Year-over-year change |
| --- | ---: | ---: | ---: |
| North | $70,145.85 | 31.17% | +18.00% |
| East | $68,377.05 | 30.39% | +43.47% |
| South | $54,405.35 | 24.18% | +18.14% |
| West | $32,103.20 | 14.27% | +9.02% |

Home Office generated **$67,499.60**, or **30.0%** of 2025 sales. Its gross margin was **44.2%**, versus **50.2%** in Everyday. Ergonomic Chair led products with **$35,206.50** in net sales, followed by Travel Backpack at **$27,464.10** and Oak Side Table at **$22,670.55**. Revenue rank alone does not establish the best promotional return, since advertising spend and fulfillment costs are absent.

## Returns by channel

| 2025 channel | Returned / all orders | Return rate |
| --- | ---: | ---: |
| Marketplace | 25 / 335 | 7.46% |
| Online | 45 / 954 | 4.72% |
| Retail | 22 / 731 | 3.01% |

Prioritize a sample review of marketplace product descriptions, packing quality and return reasons. The dataset does not record return reasons, so none should be asserted as the cause.

## Recommended next steps

1. **Supply planning:** Compare East stock-outs, lead times and forecasts with North. Use this to decide where extra inventory would reduce missed sales.
2. **Margin review:** Break down Home Office gross margin by SKU and discount bucket. Pilot a narrower discount on low-margin products and monitor units and profit, not sales alone.
3. **Return investigation:** Request structured return-reason data for Marketplace and benchmark by product. Fix the leading verified cause and remeasure return rate after the change.

## Method and limitations

Rows come from `data/orders.csv`, built deterministically by `scripts/build.py`. All values are simulated; no public or private company dataset was used. All returns are modeled as full reversals; partial returns, fees, shipping, taxes, ad spend and customer-level retention are out of scope. Calculations and filters are described in the repository README. Recommendations are analytical hypotheses that require validation with real operational records.
