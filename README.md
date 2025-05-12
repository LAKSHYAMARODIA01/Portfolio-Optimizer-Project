# 📈 Portfolio Optimizer Project

This project helps investors **optimize asset selection** using the **0/1 Knapsack algorithm** based on capital, expected returns, and risk scores. It allows filtering based on risk thresholds and visualizing the efficient frontier of risk vs. return.

## 📂 Project Structure

```
Portfolio_Optimizer_Project/
├── assets.csv                 # Sample dataset of assets
├── optimizer.py               # Core logic for portfolio optimization
├── test_optimizer.py          # Unit tests for optimizer
├── requirements.txt           # Dependency list for the project
├── frontier.png               # (Optional) Output plot of efficient frontier
└── README.md                  # This documentation
```

## 📘 Features

- 📊 Select best assets under capital using the 0/1 Knapsack algorithm
- ⚠️ Filter assets by total risk score
- 📉 Visualize risk-return tradeoff (efficient frontier)
- ✅ Includes unit tests

## 🧠 Algorithm Explanation

### 🔢 0/1 Knapsack Algorithm

- **Weight** = Price
- **Value** = Expected Return (%)
- Dynamic programming is used to maximize returns without exceeding capital.

### ⚠️ Risk Filtering

- Filters assets until total risk is under the given limit.

### 📈 Efficient Frontier

- Graph showing risk vs expected return to visualize trade-offs.

## 🔧 Requirements

Install dependencies with:

```
pip install -r requirements.txt
```

## 🧪 Run Unit Tests

```
python test_optimizer.py
```

## 🛠️ Run the Optimizer

```
python optimizer.py --capital <CAPITAL> --risk <MAX_RISK> [--csv <FILE>] [--plot]
```

Example:

```
python optimizer.py --capital 5000 --risk 40 --plot
```

## 📑 Files

### optimizer.py

Contains:
- knapsack
- filter_risk
- total_cost
- total_return
- total_risk
- plot_frontier
- main()

### test_optimizer.py

Unit tests:
- test_knapsack_basic
- test_risk_filtering
- test_total_cost_and_return

### assets.csv

Sample dataset of assets.

### requirements.txt

Dependencies:
- pandas
- matplotlib

## 📉 Output Graph

If --plot is used, saves `frontier.png` with risk vs return curve.
