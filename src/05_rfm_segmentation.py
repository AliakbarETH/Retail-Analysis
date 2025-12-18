import pandas as pd
import os
from datetime import timedelta

df = pd.read_parquet("/Users/hamza/Documents/Projects/data/processed/cleaned.parquet")

'''

We would do RFM analysis - better for customer loyality in long term and gain meaningful insights to design customer marketing campaigns
and offers.

R stands for reciency
F stands for frequency
M stands for monetry

Our dataset has return orders as well so we would like to exclude them since we want a positive number.

1) Exclude returns
2) Define analysis date
3) Compute RFM metrics
4) Score Customers ( RFM scores - range[1-5])
5) Combine RFM scores
6) Create business friendly customer segmentation
7)  Saving outputs

'''
# print(df.head())
# Excluding returns


df = df[df['Quantity'] > 0].copy()

# Defining analysis datetime for reciency = lastday + 1 day 

df['InvoiceDate'] = pd.to_datetime(df["InvoiceDate"])

analysis_date = df["InvoiceDate"].max() + timedelta(days=1)

rfm = (
    df.groupby("Customer ID")
      .agg(
          Recency=("InvoiceDate", lambda x: (analysis_date - x.max()).days),
          Frequency=("Invoice", "nunique"),
          Monetary=("Revenue", "sum")
      )
      .reset_index()
      .rename(columns={"Customer ID": "CustomerID"})
)

print("RFM metrics:")
print(rfm.head())


# rfm_columns = ["CustomerID", "Recency", "Frequency", "Monetary"]

print(rfm.head())


# calculating rfm scores

rfm["R_Score"] = pd.qcut(
    rfm["Recency"],
    5,
    labels=[5, 4, 3, 2, 1]
).astype(int)

rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    5,
    labels=[1, 2, 3, 4, 5]
).astype(int)

rfm["M_Score"] = pd.qcut(
    rfm["Monetary"],
    5,
    labels=[1, 2, 3, 4, 5]
).astype(int)


# combining rfm score

rfm["RFM_Score"] = (
    rfm["R_Score"].astype(str) +
    rfm["F_Score"].astype(str) +
    rfm["M_Score"].astype(str)
)

# creating business friendly customer segmentation

def segment_customer(row):
    if row["RFM_Score"] == "555":
        return "Champions"
    elif row["R_Score"] >= 4 and row["F_Score"] >= 4:
        return "Loyal Customers"
    elif row["R_Score"] >= 4 and row["F_Score"] <= 2:
        return "Potential Loyalists"
    elif row["R_Score"] <= 2 and row["M_Score"] >= 4:
        return "At Risk High Value"
    elif row["RFM_Score"] <= "222":
        return "Lost Customers"
    else:
        return "Needs Attention"

rfm["Segment"] = rfm.apply(segment_customer, axis=1)


# saving outputs for reporting

rfm.to_csv(
    "../outputs/kpis/rfm_customer_segments.csv",
    index=False
)

print("\nRFM segmentation completed successfully.")
print(rfm.head())