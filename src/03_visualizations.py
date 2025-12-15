import pandas as pd
import matplotlib.pyplot as plt
import os

df_monthly_revenue = pd.read_csv("/Users/hamza/Documents/Projects/outputs/kpis/monthly_revenue.csv")
df_top_products_by_country = pd.read_csv("/Users/hamza/Documents/Projects/outputs/kpis/top_products_by_country.csv")
df_top_products_by_revenue = pd.read_csv("/Users/hamza/Documents/Projects/outputs/kpis/top_products_by_revenue.csv")


plt.figure(figsize=(12,6))
plt.plot(df_monthly_revenue['InvoiceMonth'], df_monthly_revenue['Revenue'])
plt.xticks(rotation=45)
plt.title("Monthly Revenue Trend")
plt.xlabel("Invoice Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("../outputs/plots/monthly_revenue.png")


plt.figure(figsize=(12,6))
plt.plot(df_top_products_by_country['Country'], df_top_products_by_country['Revenue'])
plt.title("Top 10 products by country")
plt.xlabel("Revenue")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("../outputs/plots/top_products_by_country.png")



plt.figure(figsize=(12,6))
plt.barh(
    df_top_products_by_revenue['Description'], 
    df_top_products_by_revenue['Revenue'] 
)
plt.title("Top 10 products by revenue")
plt.xlabel("Revenue")
plt.ylabel("Product Description")
plt.gca().invert_yaxis()
plt.tight_layout() 
plt.savefig("../outputs/plots/top_producrs_by_revenue.png")
plt.show()