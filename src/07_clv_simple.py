import pandas as pd
import os

# ----------------------------------------------------
# 1. Load data
# ----------------------------------------------------
df = pd.read_parquet(
    "/Users/hamza/Documents/Projects/data/processed/cleaned.parquet"
)

# ----------------------------------------------------
# 2. Basic preprocessing
# ----------------------------------------------------
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Identify returns
df["IsReturn"] = df["Quantity"] < 0

# Drop rows without Customer ID
df = df[df["Customer ID"].notna()].copy()

# IMPORTANT: Treat Customer ID as STRING (safe for values like '13085.0')
df["Customer ID"] = (
    df["Customer ID"]
    .astype(str)
    .str.replace(".0", "", regex=False)
)

# ----------------------------------------------------
# 3. Keep only non-return (sales) transactions
# ----------------------------------------------------
sales = df[~df["IsReturn"]].copy()

# ----------------------------------------------------
# 4. Customer-level aggregates
# ----------------------------------------------------
cust = (
    sales.groupby("Customer ID")
         .agg(
             total_revenue=("Revenue", "sum"),
             orders=("Invoice", "nunique"),
             first_purchase=("InvoiceDate", "min"),
             last_purchase=("InvoiceDate", "max")
         )
         .reset_index()
)

# ----------------------------------------------------
# 5. Derived metrics
# ----------------------------------------------------
# Customer tenure (avoid zero days)
cust["tenure_days"] = (
    cust["last_purchase"] - cust["first_purchase"]
).dt.days.clip(lower=1)

# Average Order Value
cust["aov"] = cust["total_revenue"] / cust["orders"]

# Purchase frequency (orders per month)
cust["orders_per_month"] = cust["orders"] / (cust["tenure_days"] / 30.0)

# ----------------------------------------------------
# 6. Simple CLV estimate (next 6 months)
# ----------------------------------------------------
cust["clv_6m"] = cust["aov"] * cust["orders_per_month"] * 6

# ----------------------------------------------------
# 7. Save outputs
# ----------------------------------------------------
output_dir = "../outputs/clv"
os.makedirs(output_dir, exist_ok=True)

output_path = f"{output_dir}/customer_clv_simple.csv"
cust.to_csv(output_path, index=False)

print(f"Saved: {output_path}")

# ----------------------------------------------------
# 8. Preview top customers by CLV
# ----------------------------------------------------
print("\nTop 10 customers by 6-month CLV:")
print(cust.sort_values("clv_6m", ascending=False).head(10))
