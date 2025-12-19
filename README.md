# 🛒 UK Retail Analytics Project  
### Customer Value, Retention Strategy & Revenue Risk

An **end-to-end retail analytics project** using real UK transaction data to drive **customer segmentation, retention strategy, revenue forecasting, and product bundling decisions**.

This project simulates how a large UK retailer (e.g., **Tesco**) could use data analytics to move from **volume-based marketing** to **value-based customer strategy**, protecting revenue and improving long-term profitability.

---

## 📌 Business Objectives

This analysis answers key commercial questions faced by retail leadership:

- Which customer segments generate the majority of revenue?
- How concentrated is revenue among customers (Pareto risk)?
- How much revenue is currently at risk due to churn?
- Which customers drive disproportionate lifetime value?
- Are newer customer cohorts retaining as well as older ones?
- Which products should be bundled to increase basket size?
- What is the expected revenue outlook for the next 6 months?

---

## 📊 Dataset Overview

- **Transactions:** 1,067,000+ retail transactions  
- **Time Period:** December 2009 – December 2011  
- **Geography:** UK + international customers  
- **Fields:**
  - Invoice Number  
  - Product Description  
  - Quantity  
  - Unit Price  
  - Customer ID  
  - Country  
  - Transaction Date  

---

## 🧠 Analytics Techniques Used

- Data cleaning & feature engineering (Python, Pandas)
- KPI extraction & revenue metrics
- RFM customer segmentation
- Customer Lifetime Value (CLV) modeling
- Revenue concentration (Pareto) analysis
- Cohort retention analysis
- Market basket analysis (association rules)
- Time-series revenue forecasting
- Translation of analytics into business decisions
- Tableau-ready output datasets

---

## 📊 Business Analysis & Insights

### 1️⃣ Which customer segments deserve immediate retention focus?

**Answer:**  
Retention efforts should prioritize **Champions**, **Loyal Customers**, and **At-Risk High Value** segments.

| Segment            | Revenue Share |
|--------------------|---------------|
| Champions          | 54.9%         |
| Loyal Customers    | 18.9%         |
| Needs Attention    | 14.6%         |
| At-Risk High Value | 7.1%          |
| Lost Customers     | 2.6%          |

**📌 Insight**  
- **Champions + Loyal Customers generate ~73.8% of total revenue**
- **At-Risk High Value customers** contribute meaningful revenue but show declining engagement

**💡 Business Action**
- Protect Champions with loyalty rewards and personalized offers  
- Launch win-back campaigns for At-Risk High Value customers  
- Deprioritize Lost Customers due to low revenue contribution  

---

### 2️⃣ How concentrated is revenue among customers (Pareto risk)?

**Answer:**  
Revenue is **highly concentrated** among a small subset of customers.

**Evidence**
- **Top 20% of customers generate ~80.6% of total revenue**

**📌 Insight**  
A small churn event among high-value customers could materially impact revenue.

**💡 Business Action**
- Closely monitor high-value customers  
- Justify investment in CRM, loyalty programs, and churn prediction  

---

### 3️⃣ How much revenue is currently at risk?

**Answer:**  
A significant portion of revenue is exposed to churn.

**Evidence**
- **Revenue at risk (At-Risk + Lost segments): £2,016,350**

**📌 Insight**  
Revenue risk should be assessed by **value**, not customer count.

**💡 Business Action**
- Allocate retention budget based on revenue impact  
- Use declining recency and frequency as early churn signals  

---

### 4️⃣ Which customers drive disproportionate lifetime value (CLV)?

**Answer:**  
A very small number of customers generate **exceptionally high projected CLV**.

**Evidence**
- Top customers show **6-month projected CLV exceeding £7M**
- Many high-CLV customers have **short tenure but very high order value**

**📌 Insight**  
Not all customers should be treated equally.

**💡 Business Action**
- Identify and protect VIP customers  
- Offer concierge-level service or exclusive benefits  

---

### 5️⃣ Are customer cohorts showing declining retention?

**Answer:**  
Yes — recent cohorts show **lower long-term retention**.

| Cohort Month | Avg Retention |
|-------------|---------------|
| 2010-12     | 8.0%          |
| 2010-11     | 11.6%         |
| 2010-10     | 13.5%         |

**📌 Insight**  
Customers acquired in late-2010 retained poorly compared to earlier cohorts.

**💡 Business Action**
- Review acquisition channels and onboarding experience  
- Improve first-purchase and post-purchase engagement  

---

### 6️⃣ Which products should be bundled together?

**Answer:**  
Clear product affinity exists between specific SKUs.

**Top Bundles (Market Basket Analysis)**
- *Pink Blue Felt Craft Trinket Box* ↔ *Pink Cream Felt Craft Trinket Box* (Lift: 12.35)
- *Charlotte Bag Suki Design* ↔ *Red Retrospot Charlotte Bag* (Lift: 11.99)
- *Woodland Charlotte Bag* ↔ *Strawberry Charlotte Bag*

**📌 Insight**  
Customers buying one item are **10–12× more likely** to buy its paired product.

**💡 Business Action**
- Introduce bundle pricing  
- Cross-sell during checkout  
- Optimize shelf placement and recommendations  

---

### 7️⃣ What is the expected revenue outlook for the next 6 months?

**Answer:**  
Revenue is forecasted to remain strong but exposed to churn risk.

**Forecast**
- **Average monthly revenue:** £839,507  
- **Total 6-month forecast:** £5,037,040  

**📌 Insight**  
Forecasts are achievable **only if retention risk is actively managed**.

**💡 Business Action**
- Use forecast + churn risk together for planning  
- Protect forecasted revenue via retention initiatives  

---

### 8️⃣ What would a UK retailer do differently after this analysis?

**Strategic Shift**
- Volume-based marketing → **Value-based targeting**
- Aggressively protect the top 20% of customers
- Monitor cohort health monthly
- Bundle high-affinity products to increase basket size
- Use revenue forecasts alongside churn risk metrics

---

## 🧠 What This Project Demonstrates

- End-to-end retail analytics (cleaning → modeling → insights)
- RFM segmentation & customer strategy
- CLV modeling and revenue concentration analysis
- Cohort retention analysis
- Market basket analysis (association rules)
- Revenue forecasting
- Translating analytics into **clear business decisions**

---

## 📁 Project Structure

```text
src/
├── 01_data_clean.py
├── 02_Extracting_KPIs.py
├── 05_rfm_segmentation.py
├── 06_rfm_visuals.py
├── 07_clv_simple.py
├── 08_cohort_retention.py
├── 09_market_basket.py
├── 10_forecast_revenue.py
├── 11_business_insights.py
└── run_full_pipeline.py

outputs/
├── kpis/
├── insights/
├── cohort/
├── basket/
├── forecast/
└── dashboard/
