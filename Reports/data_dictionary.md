# Mutual Fund Analytics - Data Dictionary

## 01_fund_master.csv

| Column       | Data Type | Description                   |
| ------------ | --------- | ----------------------------- |
| amfi_code    | Integer   | Unique AMFI scheme identifier |
| scheme_name  | Text      | Mutual fund scheme name       |
| fund_house   | Text      | Asset management company      |
| category     | Text      | Fund category                 |
| sub_category | Text      | Fund sub-category             |
| plan         | Text      | Direct or Regular plan        |
| risk_grade   | Text      | Risk classification           |

## 02_nav_history.csv

| Column    | Data Type | Description       |
| --------- | --------- | ----------------- |
| amfi_code | Integer   | Scheme identifier |
| date      | Date      | NAV date          |
| nav       | Decimal   | Net Asset Value   |

## 07_scheme_performance.csv

| Column            | Data Type | Description                      |
| ----------------- | --------- | -------------------------------- |
| return_1yr_pct    | Decimal   | 1-year return percentage         |
| return_3yr_pct    | Decimal   | 3-year return percentage         |
| return_5yr_pct    | Decimal   | 5-year return percentage         |
| alpha             | Decimal   | Excess return over benchmark     |
| beta              | Decimal   | Volatility compared to benchmark |
| sharpe_ratio      | Decimal   | Risk-adjusted return measure     |
| expense_ratio_pct | Decimal   | Annual expense ratio             |
| aum_crore         | Decimal   | Assets under management          |

## 08_investor_transactions.csv

| Column             | Data Type | Description                 |
| ------------------ | --------- | --------------------------- |
| investor_id        | Text      | Unique investor identifier  |
| transaction_date   | Date      | Date of transaction         |
| transaction_type   | Text      | SIP, Lumpsum, or Redemption |
| amount_inr         | Decimal   | Transaction amount in INR   |
| state              | Text      | Investor state              |
| city               | Text      | Investor city               |
| city_tier          | Text      | Tier classification         |
| age_group          | Text      | Investor age category       |
| gender             | Text      | Investor gender             |
| annual_income_lakh | Decimal   | Annual income in lakhs      |
| payment_mode       | Text      | Payment method              |
| kyc_status         | Text      | KYC verification status     |

## Data Sources

* AMFI Mutual Fund Data
* MFAPI NAV Data
* Bluestock Mutual Fund Analytics Dataset

## Database

SQLite Database: bluestock_mf.db

## Processed Files

* 02_nav_history_clean.csv
* 07_scheme_performance_clean.csv
* 08_investor_transactions_clean.csv
