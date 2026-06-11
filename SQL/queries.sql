-- 1. Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV by Fund
SELECT amfi_code, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3. Transactions by State
SELECT state, COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY state
ORDER BY transaction_count DESC;

-- 4. Funds with Expense Ratio Below 1%
SELECT amfi_code, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 5. Top 5 Funds by 3-Year Return
SELECT amfi_code, return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 5;

-- 6. Top 5 Funds by Sharpe Ratio
SELECT amfi_code, sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 7. Average Transaction Amount by State
SELECT state, AVG(amount_inr) AS avg_amount
FROM fact_transactions
GROUP BY state;

-- 8. KYC Status Distribution
SELECT kyc_status, COUNT(*) AS investors
FROM fact_transactions
GROUP BY kyc_status;

-- 9. Transaction Type Distribution
SELECT transaction_type, COUNT(*) AS total
FROM fact_transactions
GROUP BY transaction_type;

-- 10. Average AUM by Fund Category
SELECT category, AVG(aum_crore) AS avg_aum
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
GROUP BY category;
