# 🛒 UK Retail Analytics Project  
### Customer Value, Retention Strategy & Revenue Risk

An **end-to-end retail analytics project** built on real UK retail transaction data, designed to support **customer segmentation, retention strategy, revenue forecasting, and product bundling decisions**.

This project simulates how a large UK retailer (e.g., **Tesco**) can shift from **volume-based marketing** to a **value-based customer strategy**, protecting revenue while improving long-term profitability.

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
- **Key Fields:**
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
- Business insight generation
- Tableau-ready dataset preparation

---

## 🛠️ Local Setup & How to Run the Project

This project is implemented as a **fully automated analytics pipeline**.  
All cleaning, analysis, segmentation, forecasting, and insight generation run **end-to-end via a single Python entry point**.

---

## ✅ Prerequisites

Ensure the following are installed:

- **Python 3.9+**
- **pip**
- **Git**
- *(Optional)* Tableau Desktop / Tableau Public

Check your Python version:

```bash
python --version


Step 1: Create a Virtual Environment (Recommended)

python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

You should see (venv) in your terminal.

Step 2: Install Dependencies

pip install -r requirements.txt

If requirements.txt does not exist yet:

pip freeze > requirements.txt

Step 3: Run the Full Analytics Pipeline

Navigate to the src directory:

cd src


Run the full pipeline with a single command:

python main.py

What the Pipeline Does

The pipeline executes the following steps in sequence:

🧹 Data Cleaning

Cleans raw transaction data

Handles missing values, cancellations, and returns

Normalizes dates and monetary fields

📊 KPI Extraction

Revenue & net revenue

Average Order Value (AOV)

Customer counts

Monthly performance trends

📈 Exploratory Visualizations

Revenue trends over time

Product-level performance insights

📤 Tableau Export

Prepares clean, analytics-ready CSV files

Optimized for Tableau dashboards

🧠 Advanced Analytics

RFM segmentation

Customer Lifetime Value (CLV)

Cohort retention analysis

Market basket analysis

Revenue forecasting

💡 Business Insights

Revenue at risk

Pareto (80/20) concentration analysis

Retention priority segments

Declining customer cohorts

Product bundling recommendations

Forecasted revenue exposure

If successful, you will see:

🎉 Pipeline completed successfully

Outputs

All results are automatically saved to the outputs/ directory:

outputs/
├── kpis/           # KPI summaries
├── insights/       # Business-ready insight tables
├── cohort/         # Cohort retention matrices
├── basket/         # Market basket rules
├── forecast/       # Revenue forecasts
├── plots/          # Python-generated visuals
└── dashboard/      # Tableau-ready datasets

Business Analysis & Key Insights
1️⃣ Which customer segments deserve immediate retention focus?

Answer:
Retention efforts should prioritize Champions, Loyal Customers, and At-Risk High Value segments.

Segment	Revenue Share
Champions	54.9%
Loyal Customers	18.9%
Needs Attention	14.6%
At-Risk High Value	7.1%
Lost Customers	2.6%

Insight

Champions and Loyal Customers generate ~73.8% of total revenue

At-Risk High Value customers represent meaningful but vulnerable revenue

Business Action

Protect top segments with loyalty rewards and personalization

Launch targeted win-back campaigns

Deprioritize Lost Customers

2️⃣ How concentrated is revenue (Pareto risk)?

Answer:
Revenue is highly concentrated.

Top 20% of customers generate ~80.6% of total revenue

Business Action

Invest in CRM, loyalty programs, and churn prevention for high-value customers

3️⃣ How much revenue is currently at risk?

Answer:

Revenue at risk (At-Risk + Lost): £2,016,350

Business Action

Allocate retention budgets based on revenue impact, not customer count

4️⃣ Which customers drive disproportionate lifetime value?

Answer:
A very small number of customers generate exceptionally high projected CLV.

Some customers exceed £7M projected CLV over 6 months

Business Action

Identify VIP customers

Offer exclusive benefits and proactive engagement

5️⃣ Are customer cohorts showing declining retention?

Answer:
Yes — newer cohorts retain less effectively.

Cohort Month	Avg Retention
2010-12	8.0%
2010-11	11.6%
2010-10	13.5%

Business Action

Review acquisition channels

Improve onboarding and early engagement

6️⃣ Which products should be bundled?

Answer:
Strong product affinity exists.

Top Bundles

Pink Blue Felt Craft Trinket Box ↔ Pink Cream Felt Craft Trinket Box (Lift: 12.35)

Charlotte Bag Suki Design ↔ Red Retrospot Charlotte Bag (Lift: 11.99)

Woodland Charlotte Bag ↔ Strawberry Charlotte Bag

Business Action

Introduce bundle pricing

Cross-sell at checkout

Optimize shelf placement

7️⃣ What is the 6-month revenue outlook?

Forecast

Average monthly revenue: £839,507

6-month forecast: £5,037,040

Insight
Forecasts are achievable only if retention risk is actively managed.

📊 Tableau Worksheets

This project includes Tableau-ready datasets designed for executive dashboards covering revenue, customer value, retention, and risk.

⬇️ Insert Tableau dashboard image below

[ Tableau Dashboard Image Placeholder ]

🧠 What This Project Demonstrates

End-to-end retail analytics pipeline

RFM segmentation and customer strategy

CLV modeling and Pareto analysis

Cohort retention analytics

Market basket analysis

Revenue forecasting

Translation of analytics into clear business decisions

📁 Project Structure
src/
├── 01_data_clean.py
├── 02_Extracting_KPIs.py
├── 03_visualizations.py
├── 04_export_for__tableau_dashboard.py
├── 05_rfm_segmentation.py
├── 06_rfm_visuals.py
├── 07_clv_simple.py
├── 08_cohort_retention.py
├── 09_market_basket.py
├── 10_forecast_revenue.py
├── 11_business_insights.py
├── run_rfm_pipeline.py
└── main.py


📌 Status: Production-ready analytics project
📊 Audience: Data Analysts, Data Scientists, Business & Product Leaders