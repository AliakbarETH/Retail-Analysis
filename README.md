# 🛒 UK Retail Analytics Project — Customer Value, Retention & Revenue Risk

An **end-to-end retail analytics project** using real UK transaction data to drive **customer segmentation, retention strategy, revenue forecasting, and product bundling decisions**.

This project simulates how a UK retailer (e.g., **Tesco**) could leverage data analytics to improve **customer retention, revenue stability, and marketing efficiency**.

---

## 📌 Business Objectives

This project answers key commercial questions:

- Which customer segments drive the majority of revenue?
- Which customers are at risk of churn and revenue loss?
- What is the expected revenue risk over the next 6 months?
- Which products should be bundled to increase basket size?
- Which customer cohorts show declining retention?
- Which customers contribute disproportionately high lifetime value?

---

## 📊 Dataset Overview

- **Transactions:** 1,067,000+ retail transactions  
- **Time Range:** December 2009 – December 2011  
- **Geography:** UK + international customers  
- **Data Fields:**  
  - Invoice  
  - Product  
  - Quantity  
  - Price  
  - Customer ID  
  - Country  
  - Date  

---

## 🧠 Analytics Techniques Used

- Data cleaning & feature engineering (Python, Pandas)
- KPI extraction & business metrics
- RFM customer segmentation
- Customer Lifetime Value (CLV) modeling
- Cohort retention analysis
- Market basket analysis (association rules)
- Revenue forecasting (time series)
- Business-driven insight generation
- Tableau-ready dashboard datasets

---

## 🔑 Key Business Insights (With Numbers)

### 1️⃣ Revenue Concentration & Customer Segments

| Segment             | Revenue Share |
|---------------------|---------------|
| Champions           | 54.9%         |
| Loyal Customers     | 18.9%         |
| Needs Attention     | 14.6%         |
| At Risk High Value  | 7.1%          |
| Lost Customers      | 2.6%          |

**📌 Insight**  
Over **73% of total revenue** comes from just **two segments** (Champions + Loyal), confirming a strong **Pareto effect**.

**💡 Business Action**
- Prioritize retention campaigns for **Champions & Loyal Customers**
- Launch targeted win-back offers for **At Risk High Value** customers

---

### 2️⃣ Revenue at Risk

- **Revenue at risk from At-Risk & Lost customers:**  
  **💰 £2,016,350**

**📌 Insight**  
If at-risk customers churn completely, the retailer risks losing **~£2M in revenue**.

**💡 Business Action**
- Trigger early churn-prevention campaigns
- Offer personalized incentives based on RFM scores

---

### 3️⃣ Customer Lifetime Value (CLV)

Top customers show **extremely high projected 6-month CLV**.

**Example:**
- **Customer 15098 → £7.18M projected CLV (6 months)**

**📌 Insight**  
A very small group of customers drives **disproportionate long-term value**.

**💡 Business Action**
- Create VIP loyalty tiers
- Assign premium service & exclusive offers to high-CLV customers

---

### 4️⃣ Retention & Cohort Analysis

**Lowest Retention Cohorts**

| Cohort Month | Avg Retention |
|-------------|---------------|
| 2010-12     | 8.0%          |
| 2010-11     | 11.6%         |
| 2010-10     | 13.5%         |

**📌 Insight**  
Customers acquired in **late-2010** show very poor long-term retention.

**💡 Business Action**
- Review acquisition channels used during these periods
- Improve onboarding and post-purchase engagement

---

### 5️⃣ Product Bundling (Market Basket Analysis)

**High-Confidence Product Bundles**

- **PINK BLUE FELT CRAFT TRINKET BOX**  
  ↔ **PINK CREAM FELT CRAFT TRINKET BOX**  
  *Lift: 12.35*

- **CHARLOTTE BAG SUKI DESIGN**  
  ↔ **RED RETROSPOT CHARLOTTE BAG**  
  *Lift: 11.99*

**📌 Insight**  
Customers buying one product are **10–12× more likely** to buy its paired product.

**💡 Business Action**
- Bundle these products in promotions
- Place them together in-store and online recommendations

---

### 6️⃣ Revenue Forecast (Next 6 Months)

- **Forecasted Avg Monthly Revenue:** £839,507  
- **Forecasted 6-Month Revenue:** £5.04M  

**📌 Insight**  
Revenue forecasting enables **early downside-risk detection**.

**💡 Business Action**
- Adjust marketing spend and inventory planning
- Use forecasts for quarterly revenue planning

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
