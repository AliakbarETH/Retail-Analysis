import pandas as pd
import os
from prophet import Prophet

df = pd.read_parquet("../data/processed/cleaned.parquet")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["IsReturn"] = df["Quantity"] < 0

# Net revenue monthly = sales - returns
df["InvoiceMonth"] = df["InvoiceDate"].dt.to_period("M").dt.to_timestamp()

monthly = (df.groupby(["InvoiceMonth", "IsReturn"])["Revenue"]
           .sum()
           .unstack(fill_value=0)
           .reset_index())

monthly["NetRevenue"] = monthly[False] - monthly[True]
monthly = monthly.rename(columns={"InvoiceMonth":"ds", "NetRevenue":"y"})

m = Prophet()
m.fit(monthly[["ds","y"]])

future = m.make_future_dataframe(periods=6, freq="MS")
forecast = m.predict(future)

os.makedirs("../outputs/forecast", exist_ok=True)
monthly.to_csv("../outputs/forecast/monthly_net_revenue.csv", index=False)
forecast.to_csv("../outputs/forecast/forecast_output.csv", index=False)

print("Saved forecast outputs in outputs/forecast/")
