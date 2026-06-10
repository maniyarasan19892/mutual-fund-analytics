import pandas as pd
from pathlib import Path

data_path = Path("data/raw")

csv_files = sorted(data_path.glob("*.csv"))

print("=" * 80)
print("MUTUAL FUND ANALYTICS - DATA INGESTION")
print("=" * 80)

for file in csv_files:

    print("\n" + "=" * 80)
    print(f"FILE: {file.name}")

    df = pd.read_csv(file)

    print(f"\nShape: {df.shape}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

print("\nAll datasets loaded successfully!")