import pandas as pd
import os

df = pd.read_parquet("/Users/hamza/Documents/Projects/data/processed/cleaned.parquet")

os.makedirs("../outputs/kpis", exist_ok=True)

'''
Key KPIs:
    a) Total Revenue 
    b) Total Sales (after excluding returns)
    c) Total Returns Revenue
    d) Net Revenue
    e) Average Order Value (AOV)
    f) Number of Unique Customers
    g) Monthly Revenue
    h) Top Products in Revenue
'''

print(df.head(10))

# Total Revenue

total_revenue = df['Revenue'].sum()

# Total Sales (after excluding returns)

sales_revenue = df[df['Quantity'] > 0]['Revenue'].sum()

# Total Returns Revenue

return_revenue = df[df['Quantity'] < 0]['Revenue'].sum()

# Net Revenue

net_revenue = sales_revenue - return_revenue

# Average Order Value (AOV)

num_orders = df['Invoice'].nunique()
aov = total_revenue/num_orders

#  Number of Unique Customers

num_customers = df['Customer ID'].nunique()

# Monthly Revenue

df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M').astype(str)
monthly_revenue = df.groupby('InvoiceMonth')['Revenue'].sum()
monthly_revenue.head()

#Top Products in Revenue

top_products_by_revenue = (
    df.groupby('Description', as_index=False)['Revenue']
    .sum()
    .sort_values(by='Revenue', ascending=False)
    .head(10)
)

revenue_by_country = (
    df.groupby('Country')['Revenue']
      .sum()
      .sort_values(ascending=False)
)


monthly_revenue.to_csv("../outputs/kpis/monthly_revenue.csv", index=True)
top_products_by_revenue.to_csv("../outputs/kpis/top_products_by_revenue.csv", index=False)
revenue_by_country.to_csv("../outputs/kpis/top_products_by_country.csv")