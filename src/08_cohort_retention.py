import pandas as pd
import numpy as np
import os

# ----------------------------------------------------
# 1. Load data
# ----------------------------------------------------
df = pd.read_parquet("../data/processed/cleaned.parquet")

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
# 3. Keep only non-return transactions
# ----------------------------------------------------
sales = df[~df["IsReturn"]].copy()

# ----------------------------------------------------
# 4. Create invoice & cohort months
# ----------------------------------------------------
sales["InvoiceMonth"] = sales["InvoiceDate"].dt.to_period("M")

sales["CohortMonth"] = (
    sales.groupby("Customer ID")["InvoiceMonth"]
         .transform("min")
)

# ----------------------------------------------------
# 5. Cohort index (months since first purchase)
# ----------------------------------------------------
def cohort_index(df_):
    year_diff = df_["InvoiceMonth"].dt.year - df_["CohortMonth"].dt.year
    month_diff = df_["InvoiceMonth"].dt.month - df_["CohortMonth"].dt.month
    return year_diff * 12 + month_diff + 1

sales["CohortIndex"] = cohort_index(sales)

# ----------------------------------------------------
# 6. Build cohort table
# ----------------------------------------------------
cohort_data = (
    sales.groupby(["CohortMonth", "CohortIndex"])["Customer ID"]
          .nunique()
          .reset_index(name="Customers")
)

cohort_pivot = cohort_data.pivot(
    index="CohortMonth",
    columns="CohortIndex",
    values="Customers"
)

# ----------------------------------------------------
# 7. Retention calculation
# ----------------------------------------------------
cohort_size = cohort_pivot.iloc[:, 0]
retention = cohort_pivot.divide(cohort_size, axis=0)

# ----------------------------------------------------
# 8. Save outputs
# ----------------------------------------------------
output_dir = "../outputs/cohort"
os.makedirs(output_dir, exist_ok=True)

cohort_pivot.to_csv(f"{output_dir}/cohort_counts.csv")
retention.to_csv(f"{output_dir}/cohort_retention_pct.csv")

print("Saved cohort outputs in outputs/cohort/")
print("\nCohort counts (head):")
print(cohort_pivot.head())
print("\nCohort retention % (head):")
print(retention.head())
