import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///data/processed/bluestock_mf.db")

# Load cleaned files

pd.read_csv(
    "data/processed/02_nav_history_clean.csv"
).to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/08_investor_transactions_clean.csv"
).to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/07_scheme_performance_clean.csv"
).to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/raw/01_fund_master.csv"
).to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

print("SQLite database loaded successfully")