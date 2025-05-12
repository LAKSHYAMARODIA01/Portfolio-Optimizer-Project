import unittest
import pandas as pd
from optimizer import knapsack, filter_risk, total_cost, total_return

class TestPortfolioOptimizer(unittest.TestCase):
    def setUp(self):
        self.assets = pd.DataFrame({
            "Ticker": ["A", "B", "C", "D", "E"],
            "ExpectedReturn(%)": [5, 10, 12, 6, 8],
            "RiskScore(0-100)": [20, 30, 25, 10, 15],
            "Price": [1000, 2000, 1500, 1200, 1700]
        })

    def test_knapsack_basic(self):
        capital = 3500
        selected = knapsack(self.assets, capital)
        expected = set(["B", "C"])  # Example best fit for test data
        self.assertEqual(set(selected), expected)

    def test_risk_filtering(self):
        capital = 5000
        selected = knapsack(self.assets, capital)
        filtered = filter_risk(selected, self.assets, 30)
        total_r = self.assets[self.assets["Ticker"].isin(filtered)]["RiskScore(0-100)"].sum()
        self.assertLessEqual(total_r, 30)

    def test_total_cost_and_return(self):
        selected = knapsack(self.assets, 10000)
        cost = total_cost(self.assets, selected)
        ret = total_return(self.assets, selected)
        self.assertGreater(cost, 0)
        self.assertGreater(ret, 0)


if __name__ == '__main__':
    unittest.main()
