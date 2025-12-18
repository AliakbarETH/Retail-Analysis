import pandas as pd
from pathlib import Path

# -----------------------------
# Paths (robust)
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
BASE_OUTPUT = BASE_DIR / "outputs"
INSIGHTS_DIR = BASE_OUTPUT / "insights"
INSIGHTS_DIR.mkdir(exist_ok=True)

# -----------------------------
# Load required datasets (FIXED PATHS)
# -----------------------------
rfm = pd.read_csv(BASE_OUTPUT / "kpis" / "rfm_customer_segments.csv")
clv = pd.read_csv(BASE_OUTPUT / "clv" / "customer_clv_simple.csv")
cohort_retention = pd.read_csv(
    BASE_OUTPUT / "cohort" / "cohort_retention_pct.csv", index_col=0
)
assoc_rules = pd.read_csv(BASE_OUTPUT / "basket" / "association_rules.csv")
forecast = pd.read_csv(BASE_OUTPUT / "forecast" / "forecast_output.csv")

# -----------------------------
# 1️⃣ Revenue by RFM Segment
# -----------------------------
segment_revenue = (
    rfm.groupby("Segment")["Monetary"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

segment_revenue["RevenueSharePct"] = (
    segment_revenue["Monetary"] / segment_revenue["Monetary"].sum() * 100
)

segment_revenue.to_csv(INSIGHTS_DIR / "segment_revenue.csv", index=False)

# -----------------------------
# 2️⃣ Retention Priority Segments
# -----------------------------
retention_priority = segment_revenue[
    segment_revenue["Segment"].isin(
        ["Champions", "Loyal Customers", "At Risk High Value"]
    )
]

retention_priority.to_csv(
    INSIGHTS_DIR / "retention_priority_segments.csv", index=False
)

# -----------------------------
# 3️⃣ Revenue Concentration (Pareto)
# -----------------------------
clv_sorted = clv.sort_values("total_revenue", ascending=False)
clv_sorted["cum_revenue_pct"] = (
    clv_sorted["total_revenue"].cumsum() / clv_sorted["total_revenue"].sum()
)

top_20_pct_customers = clv_sorted.head(int(0.2 * len(clv_sorted)))
pareto_revenue_share = (
    top_20_pct_customers["total_revenue"].sum()
    / clv_sorted["total_revenue"].sum()
    * 100
)

pd.DataFrame({
    "Metric": ["Top 20% Customers Revenue Share"],
    "Value": [round(pareto_revenue_share, 2)]
}).to_csv(INSIGHTS_DIR / "pareto_revenue_risk.csv", index=False)

# -----------------------------
# 4️⃣ Top CLV Customers
# -----------------------------
clv.sort_values("clv_6m", ascending=False).head(20).to_csv(
    INSIGHTS_DIR / "top_clv_customers.csv", index=False
)

# -----------------------------
# 5️⃣ Declining Cohorts
# -----------------------------
declining_cohorts = (
    cohort_retention.iloc[:, 1:]
    .mean(axis=1)
    .sort_values()
    .head(5)
    .reset_index()
)

declining_cohorts.columns = ["CohortMonth", "AvgRetentionRate"]

declining_cohorts.to_csv(
    INSIGHTS_DIR / "declining_cohorts.csv", index=False
)

# -----------------------------
# 6️⃣ Product Bundling Opportunities
# -----------------------------
assoc_rules[
    (assoc_rules["lift"] > 5) &
    (assoc_rules["confidence"] > 0.4)
].sort_values("lift", ascending=False).head(10).to_csv(
    INSIGHTS_DIR / "top_product_bundles.csv", index=False
)

# -----------------------------
# 7️⃣ Revenue Risk
# -----------------------------
returns_risk = rfm[rfm["Segment"].str.contains("Lost|At Risk", case=False)]

pd.DataFrame({
    "Metric": ["Revenue at Risk (At-Risk & Lost Customers)"],
    "Value": [round(returns_risk["Monetary"].sum(), 2)]
}).to_csv(INSIGHTS_DIR / "revenue_at_risk.csv", index=False)

# -----------------------------
# 8️⃣ Forecast Risk (Next 6 Months)
# -----------------------------
forecast_next_6m = forecast.tail(6)

pd.DataFrame({
    "Metric": [
        "Forecasted Avg Monthly Revenue (Next 6 Months)",
        "Forecasted Total Revenue (Next 6 Months)"
    ],
    "Value": [
        round(forecast_next_6m["yhat"].mean(), 2),
        round(forecast_next_6m["yhat"].sum(), 2)
    ]
}).to_csv(INSIGHTS_DIR / "forecast_risk.csv", index=False)

# -----------------------------
# Console summary
# -----------------------------
print("\n📊 BUSINESS INSIGHTS GENERATED SUCCESSFULLY")
print("✔ Revenue by Segment")
print("✔ Retention Priority Segments")
print("✔ Pareto Revenue Risk")
print("✔ Top CLV Customers")
print("✔ Declining Cohorts")
print("✔ Product Bundles")
print("✔ Revenue at Risk")
print("✔ Forecast Risk (6 months)")
print("📁 Saved in outputs/insights/")
