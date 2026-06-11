import pandas as pd

# Load data
df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Numeric columns to validate
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

# Convert to numeric
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Check anomalies
print("\nMissing values in numeric columns:")
print(df[numeric_cols].isnull().sum())

# Validate expense ratio
anomalies = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Anomalies:")
print(anomalies[["scheme_name", "expense_ratio_pct"]])

# Remove invalid expense ratios
df = df[
    (df["expense_ratio_pct"] >= 0.1) &
    (df["expense_ratio_pct"] <= 2.5)
]

# Save cleaned file
df.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("\nRows:", len(df))
print("Scheme performance cleaned successfully")