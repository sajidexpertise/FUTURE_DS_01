"""Build deterministic demonstration data and an entirely offline dashboard.

Run from any directory: python scripts/build.py
Python standard library only.
"""
from __future__ import annotations

import csv
import json
import random
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RNG = random.Random(20260921)
PRODUCTS = [
    ("Desk Lamp", "Home Office", 58, 28, 1.55),
    ("Ergonomic Chair", "Home Office", 245, 144, 0.71),
    ("Monitor Riser", "Home Office", 72, 33, 1.27),
    ("Ceramic Dinner Set", "Kitchen", 112, 57, 0.92),
    ("Pour Over Kit", "Kitchen", 79, 38, 1.09),
    ("Cast Iron Pan", "Kitchen", 135, 80, 0.78),
    ("Linen Throw", "Living", 96, 49, 1.12),
    ("Accent Cushion", "Living", 46, 20, 1.58),
    ("Oak Side Table", "Living", 189, 112, 0.69),
    ("Travel Backpack", "Everyday", 129, 68, 1.04),
    ("Insulated Bottle", "Everyday", 42, 18, 1.67),
    ("Canvas Tote", "Everyday", 32, 12, 1.47),
]
REGIONS = ["North", "South", "East", "West"]
CHANNELS = ["Online", "Retail", "Marketplace"]
FIELDS = ["order_id", "order_date", "region", "channel", "category", "product", "units", "unit_price_usd", "discount_rate", "net_sales_usd", "cogs_usd", "gross_profit_usd", "returned"]


def make_rows():
    rows = []
    start = date(2024, 1, 1)
    end = date(2025, 12, 31)
    day = start
    order_id = 1
    while day <= end:
        season = {1: .74, 2: .79, 3: .89, 4: .97, 5: 1.02, 6: 1.07, 7: .98, 8: 1.03, 9: 1.12, 10: 1.17, 11: 1.42, 12: 1.54}[day.month]
        year = 1.16 if day.year == 2025 else 1
        weekday = 1.17 if day.weekday() in (5, 6) else 1
        volume = max(1, round(RNG.gauss(4.25 * season * year * weekday, 1.8)))
        for _ in range(volume):
            weights = [p[4] for p in PRODUCTS]
            product, category, unit_price, unit_cost, _ = RNG.choices(PRODUCTS, weights)[0]
            region = RNG.choices(REGIONS, [31, 25, 27, 17])[0]
            channel = RNG.choices(CHANNELS, [49 if day.year == 2025 else 43, 35, 16 if day.year == 2025 else 22])[0]
            units = RNG.choices([1, 2, 3, 4], [72, 20, 6, 2])[0]
            discount = RNG.choices([0, .05, .1, .15, .2], [55, 18, 14, 9, 4])[0]
            if channel == "Marketplace":
                discount = max(discount, .05)
            # Returns are retained as rows for operational analysis, but contribute
            # zero to recognized sales / COGS / profit throughout this project.
            returned = RNG.random() < (.075 if channel == "Marketplace" else .043 if channel == "Online" else .025)
            net = 0 if returned else round(unit_price * units * (1 - discount), 2)
            cost = 0 if returned else round(unit_cost * units, 2)
            rows.append(dict(order_id=f"NG-{order_id:05d}", order_date=day.isoformat(), region=region,
                             channel=channel, category=category, product=product, units=units,
                             unit_price_usd=unit_price, discount_rate=discount,
                             net_sales_usd=net, cogs_usd=cost,
                             gross_profit_usd=round(net - cost, 2), returned=returned))
            order_id += 1
        day += timedelta(days=1)
    return rows


def summarize(rows, year):
    selected = [r for r in rows if r["order_date"].startswith(str(year))]
    kept = [r for r in selected if not r["returned"]]
    sales = round(sum(r["net_sales_usd"] for r in kept), 2)
    profit = round(sum(r["gross_profit_usd"] for r in kept), 2)
    def group(field):
        out = defaultdict(lambda: {"sales": 0, "profit": 0, "orders": 0})
        for r in kept:
            x = out[r[field]]
            x["sales"] += r["net_sales_usd"]
            x["profit"] += r["gross_profit_usd"]
            x["orders"] += 1
        return {k: {n: round(v, 2) for n, v in vals.items()} for k, vals in sorted(out.items())}
    monthly = defaultdict(float)
    for r in kept:
        monthly[r["order_date"][:7]] += r["net_sales_usd"]
    return dict(year=year, orders=len(kept), returns=len(selected) - len(kept),
                return_rate=round((len(selected) - len(kept)) / len(selected), 4),
                sales=sales, profit=profit, margin=round(profit / sales, 4),
                aov=round(sales / len(kept), 2),
                monthly={k: round(v, 2) for k, v in sorted(monthly.items())},
                region=group("region"), category=group("category"),
                product=group("product"), channel=group("channel"))


def main():
    rows = make_rows()
    data = ROOT / "data"
    data.mkdir(exist_ok=True)
    with (data / "orders.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    report = {"about": "Synthetic demonstration data; no real customers or transactions.",
              "2024": summarize(rows, 2024), "2025": summarize(rows, 2025)}
    (data / "summary.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    template = (ROOT / "dashboard.template.html").read_text(encoding="utf-8")
    # Escape `<` so serialized JSON remains inert inside the script element.
    payload = json.dumps(rows, separators=(",", ":")).replace("<", "\\u003c")
    (ROOT / "index.html").write_text(template.replace("/*__DATA__*/[]", payload), encoding="utf-8")
    print(f"Generated {len(rows)} orders; 2025 sales ${report['2025']['sales']:,.2f}; "
          f"2025 gross profit ${report['2025']['profit']:,.2f}")


if __name__ == "__main__":
    main()
