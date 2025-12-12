import pandas as pd

# Read Raw Data from CSV

df = pd.read_csv("/Users/hamza/Documents/Projects/data/raw/online_retail_II.csv", encoding="ISO-8859-1")

# Fix Data types

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Fix missing Values

df["Customer ID"] = df["Customer ID"].fillna("Guest").astype(str)
df["Description"] = df["Description"].fillna("Unknown").astype(str)

# Remove exact Duplicates

df.drop_duplicates()


# Calculate Revenue

df["Revenue"] = df["Quantity"] * df["Price"]

# make a returns column

df["IsReturn"] = df["Invoice"].astype(str).str.startswith("C")

# Time Features

df["InoviceMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)
df["Year"] = df["InvoiceDate"].dt.year
df['Month'] = df['InvoiceDate'].dt.month 

# Save cleaned Version into paraquet version for faster retrieval

df.to_parquet("/Users/hamza/Documents/Projects/data/processed/cleaned.parquet", index=False)


print("Cleaning Complete! Rows:", df.shape[0])
