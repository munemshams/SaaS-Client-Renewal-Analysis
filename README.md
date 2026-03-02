**SaaS Client Renewal Analysis**

This project analyzes subscription renewal behavior for a SaaS company using three interconnected datasets:

- Client Details

- Subscription Records

- Economic Indicators

The goal is to understand:

- How many clients come from Fintech and Crypto

- Which industry has the highest renewal rate

- How macroeconomic conditions (inflation) influence renewal behavior

The insights help the company strengthen customer retention and optimize renewal strategies.

**Objectives & Insights**

1️. Total Fintech + Crypto Clients

Counts clients belonging to either industry.

Output: total_fintech_crypto_clients.txt

2️. Industry With the Highest Renewal Rate

Determined by merging client data with subscription records and computing renewal proportions.

Output: top_industry.txt
Visualization: renewal_rate_by_industry.png

3️. Average Inflation Rate at Renewal Time

Matches subscription end dates with quarterly economic indicators to identify the inflation conditions when customers renewed.

Output: average_inflation_for_renewals.txt
Visualization: inflation_rate_over_time.png

**Methodology**

The Python script:

- Loads all datasets

- Merges client + subscription data

- Computes industry renewal rates

- Uses merge_asof() to connect macroeconomic indicators based on end dates

- Generates text outputs for final answers

- Creates two visualizations:

1. Renewal rate by industry (bar chart)

2. Inflation rate trend over time (line chart)

## 📁 Files Included

| File Name | Description |
|----------|-------------|
| `saas_subscription_analysis.py` | Main Python script performing all calculations and generating visualizations. |
| `client_details.csv` | Dataset for Client demographic, industry, and company size information. |
| `subscription_records.csv` | Dataset with Subscription start/end dates and renewal flags. |
| `economic_indicators.csv` | Quarterly inflation and GDP growth dataset. |
| `total_fintech_crypto_clients.txt` | Number of clients in Fintech or Crypto industries. |
| `top_industry.txt` | Industry with the highest renewal rate. |
| `average_inflation_for_renewals.txt` | Inflation rate when renewed clients renewed their subscriptions. |
| `renewal_rate_by_industry.png` | Bar chart showing renewal rates across industries. |
| `inflation_rate_over_time.png` | Line chart showing inflation rates across quarters. |
| `README.md` | Full project documentation. |
