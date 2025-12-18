import pandas as pd
import os
from mlxtend.frequent_patterns import apriori, association_rules

# ----------------------------------------------------
# 1. Load data
# ----------------------------------------------------
df = pd.read_parquet("../data/processed/cleaned.parquet")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# ----------------------------------------------------
# 2. Remove returns
# ----------------------------------------------------
df = df[df["Quantity"] > 0].copy()

# ----------------------------------------------------
# 3. Keep UK only (optional but recommended)
# ----------------------------------------------------
df = df[df["Country"] == "United Kingdom"].copy()

# ----------------------------------------------------
# 4. Reduce dimensionality (CRITICAL FIX)
# ----------------------------------------------------
# Keep only top N products by quantity sold
TOP_N_PRODUCTS = 100   # lower if memory is tight

top_products = (
    df.groupby("Description")["Quantity"]
      .sum()
      .sort_values(ascending=False)
      .head(TOP_N_PRODUCTS)
      .index
)

df = df[df["Description"].isin(top_products)].copy()

# ----------------------------------------------------
# 5. Build basket (Invoice × Product)
# ----------------------------------------------------
basket = (
    df.groupby(["Invoice", "Description"])["Quantity"]
      .sum()
      .unstack(fill_value=0)
)

# IMPORTANT: Convert to boolean (not int)
basket = basket > 0

print(f"Basket shape: {basket.shape}")

# ----------------------------------------------------
# 6. Frequent itemsets
# ----------------------------------------------------
itemsets = apriori(
    basket,
    min_support=0.02,   # increase support to reduce combinations
    use_colnames=True
)

# ----------------------------------------------------
# 7. Association rules
# ----------------------------------------------------
rules = association_rules(
    itemsets,
    metric="lift",
    min_threshold=1.2
)

rules = rules.sort_values(["lift", "confidence"], ascending=False)

# ----------------------------------------------------
# 8. Save outputs
# ----------------------------------------------------
os.makedirs("../outputs/basket", exist_ok=True)

itemsets.to_csv("../outputs/basket/frequent_itemsets.csv", index=False)
rules.to_csv("../outputs/basket/association_rules.csv", index=False)

print("Saved: outputs/basket/frequent_itemsets.csv and association_rules.csv")
print(
    rules.head(10)[
        ["antecedents", "consequents", "support", "confidence", "lift"]
    ]
)
