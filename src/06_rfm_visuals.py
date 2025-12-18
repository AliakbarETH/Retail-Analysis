import pandas as pd
import matplotlib.pyplot as plt
import os

rfm = pd.read_csv("/Users/hamza/Documents/Projects/outputs/kpis/rfm_customer_segments.csv")

os.makedirs("../outputs/plots", exist_ok=True)

# Segment counts
seg_counts = rfm["Segment"].value_counts()

plt.figure(figsize=(10,5))
plt.bar(seg_counts.index, seg_counts.values)
plt.title("Customer Count by RFM Segment")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("../outputs/plots/rfm_segment_counts.png")
plt.close()

# Revenue contribution
seg_rev = rfm.groupby("Segment")["Monetary"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))
plt.bar(seg_rev.index, seg_rev.values)
plt.title("Revenue Contribution by RFM Segment")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("../outputs/plots/rfm_segment_revenue.png")
plt.close()

print("Saved RFM plots in outputs/plots/")
