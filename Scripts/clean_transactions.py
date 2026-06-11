import pandas as pd

# Load data
df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Fix date format
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

valid_types = ["Sip", "Lumpsum", "Redemption"]

df.loc[
    ~df["transaction_type"].isin(valid_types),
    "transaction_type"
] = "Unknown"

# Validate amount > 0
df = df[df["amount_inr"] > 0]

# Validate KYC status
df["kyc_status"] = (
    df["kyc_status"]
    .astype(str)
    .str.strip()
    .str.upper()
)

valid_kyc = ["VERIFIED", "PENDING", "REJECTED"]

print("\nKYC Values Found:")
print(df["kyc_status"].value_counts())

# Remove duplicate records
df = df.drop_duplicates()

# Save cleaned data
df.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("\nRows:", len(df))
print("Investor transactions cleaned successfully")