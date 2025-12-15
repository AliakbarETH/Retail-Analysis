import pandas as pd

df = pd.read_parquet("/Users/hamza/Documents/Projects/data/processed/cleaned.parquet")

print(df.columns)

'''
We need to create visualisation CSVs for dataset. 

So, we need :

    a) Clean Transactions
    b) Monthly Revenue
    c) Top Products
    d) Country level Revenue

'''

# Clean Transactions 

df_clean = df[[
    "Invoice", "StockCode", "Description", "Quantity", "InvoiceDate", "Price", "Revenue",
    "Country", "IsReturn", "InvoiceMonth", "Year", "Month"
    ]]

df_clean.to_csv("../outputs/dashboard/clean_transactions.csv", index=False)

# Monthly Revenue

sales_monthly = df[df["IsReturn"] == False].groupby("InvoiceMonth")["Revenue"].sum().reset_index()
sales_monthly.rename(columns={"Revenue": "SalesRevenue"}, inplace=True)

returns_monthly = df[df["IsReturn"] == True].groupby("InvoiceMonth")["Revenue"].sum().reset_index()
returns_monthly.rename(columns={"Revenue": "ReturnRevenue"}, inplace=True)

monthly = sales_monthly.merge(returns_monthly, on="InvoiceMonth", how="left")
monthly["ReturnRevenue"] = monthly["ReturnRevenue"].fillna(0)
monthly["NetRevenue"] = monthly["SalesRevenue"] - monthly["ReturnRevenue"]

monthly.to_csv("../outputs/dashboard/monthly_sales.csv", index=False)

# top products

top_products = (
    df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(20)
    .reset_index()
)

top_products.to_csv("../outputs/dashboard/top_products.csv", index=False)

# Country-level Revenue

country_rev = df.groupby("Country")["Revenue"].sum().reset_index()
country_rev.to_csv("../outputs/dashboard/country_revenue.csv", index=False)

print("Dashboard dataset exported successfully")