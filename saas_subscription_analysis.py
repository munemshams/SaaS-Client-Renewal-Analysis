import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------
# Load datasets
# -------------------------------------
client_details = pd.read_csv("client_details.csv")
subscription_records = pd.read_csv(
    "subscription_records.csv",
    parse_dates=["start_date", "end_date"]
)
economic_indicators = pd.read_csv(
    "economic_indicators.csv",
    parse_dates=["start_date", "end_date"]
)

# =====================================
# 1. Total Fintech + Crypto clients
# =====================================

total_fintech_crypto_clients = client_details[
    client_details["industry"].isin(["Fintech", "Crypto"])
].shape[0]

with open("total_fintech_crypto_clients.txt", "w") as f:
    f.write(str(total_fintech_crypto_clients))

# =====================================
# 2. Industry with the highest renewal rate
# =====================================

subscriptions = pd.merge(
    subscription_records,
    client_details,
    on="client_id",
    how="left"
)

renewal_rates = subscriptions.groupby("industry")["renewed"].mean()
top_industry = renewal_rates.idxmax()

with open("top_industry.txt", "w") as f:
    f.write(top_industry)

# Optional visualization: Renewal Rates by Industry
plt.figure(figsize=(10, 6))
renewal_rates.sort_values().plot(kind="barh", color="skyblue")
plt.title("Renewal Rate by Industry")
plt.xlabel("Renewal Rate")
plt.ylabel("Industry")
plt.tight_layout()
plt.savefig("renewal_rate_by_industry.png")
plt.close()

# =====================================
# 3. Average inflation at time of renewal
# =====================================

subscriptions_with_inflation = pd.merge_asof(
    subscription_records.sort_values("end_date"),
    economic_indicators.sort_values("start_date"),
    left_on="end_date",
    right_on="start_date",
    direction="backward"
)

average_inflation_for_renewals = (
    subscriptions_with_inflation[
        subscriptions_with_inflation["renewed"] == True
    ]["inflation_rate"]
    .mean()
)

with open("average_inflation_for_renewals.txt", "w") as f:
    f.write(str(average_inflation_for_renewals))

# Optional visualization: Inflation Rates Over Time
plt.figure(figsize=(10, 6))
plt.plot(
    economic_indicators["start_date"],
    economic_indicators["inflation_rate"],
    marker="o",
    linestyle="-",
    color="orange"
)
plt.title("Inflation Rate Over Time")
plt.xlabel("Quarter")
plt.ylabel("Inflation Rate")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("inflation_rate_over_time.png")
plt.close()

# =====================================
# Console output
# =====================================
print("\nResults Generated:")
print("Total Fintech & Crypto clients:", total_fintech_crypto_clients)
print("Industry with highest renewal rate:", top_industry)
print("Average inflation at time of renewal:", average_inflation_for_renewals)

print("\nFiles created:")
print("- total_fintech_crypto_clients.txt")
print("- top_industry.txt")
print("- average_inflation_for_renewals.txt")
print("- renewal_rate_by_industry.png")
print("- inflation_rate_over_time.png")
