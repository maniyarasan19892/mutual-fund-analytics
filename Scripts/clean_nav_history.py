import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Sort
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# Forward fill NAV
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Keep valid NAV values
df = df[df["nav"] > 0]

# Remove bad dates if any
df = df.dropna(subset=["date"])

# Save
df.to_csv(
    "data/processed/02_nav_history_clean.csv",
    index=False
)

print("Rows:", len(df))
print("NAV history cleaned successfully")