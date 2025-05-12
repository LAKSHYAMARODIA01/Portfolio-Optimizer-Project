import pandas as pd
import argparse
import matplotlib.pyplot as plt


def knapsack(assets, capital):
    assets = assets.copy()
    assets["ExpectedReturn(%)"] = assets["ExpectedReturn(%)"].astype(float)
    assets["Price"] = assets["Price"].astype(int)
    n = len(assets)
    C = int(capital)
    dp = [[0] * (C + 1) for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):
        price = int(assets.iloc[i - 1]["Price"])
        ret = float(assets.iloc[i - 1]["ExpectedReturn(%)"])
        for w in range(C + 1):
            if price <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - price] + ret)
            else:
                dp[i][w] = dp[i - 1][w]

    # Traceback selected items
    w = C
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(assets.iloc[i - 1]["Ticker"])
            w -= int(assets.iloc[i - 1]["Price"])

    return selected[::-1]


def filter_risk(selected_tickers, assets_df, max_risk):
    selected_df = assets_df[assets_df["Ticker"].isin(selected_tickers)].copy()
    while selected_df["RiskScore(0-100)"].sum() > max_risk:
        worst_asset = selected_df.sort_values("ExpectedReturn(%)").iloc[0]
        selected_tickers.remove(worst_asset["Ticker"])
        selected_df = assets_df[assets_df["Ticker"].isin(selected_tickers)]
    return selected_tickers


def total_cost(assets_df, tickers):
    return assets_df[assets_df["Ticker"].isin(tickers)]["Price"].sum()


def total_return(assets_df, tickers):
    return assets_df[assets_df["Ticker"].isin(tickers)]["ExpectedReturn(%)"].sum()


def total_risk(assets_df, tickers):
    return assets_df[assets_df["Ticker"].isin(tickers)]["RiskScore(0-100)"].sum()


def plot_frontier(assets_df, capital):
    risks = []
    returns = []

    for r in range(0, 101, 5):
        selected = knapsack(assets_df, capital)
        filtered = filter_risk(selected, assets_df, r)
        ret = total_return(assets_df, filtered)
        risk = total_risk(assets_df, filtered)
        risks.append(risk)
        returns.append(ret)

    plt.figure(figsize=(8, 6))
    plt.scatter(risks, returns, color='blue')
    plt.title("Efficient Frontier")
    plt.xlabel("Risk Score")
    plt.ylabel("Expected Return (%)")
    plt.grid(True)
    plt.savefig("frontier.png")
    plt.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--capital", type=int, required=True)
    parser.add_argument("--risk", type=int, required=True)
    parser.add_argument("--csv", type=str, default="assets.csv")
    parser.add_argument("--plot", action="store_true")
    args = parser.parse_args()

    assets = pd.read_csv(args.csv)
    selected = knapsack(assets, args.capital)
    filtered = filter_risk(selected, assets, args.risk)

    cost = total_cost(assets, filtered)
    ret = total_return(assets, filtered)
    risk = total_risk(assets, filtered)

    print(f"Selected {len(filtered)} assets:\n" + "  ".join(filtered))
    print(f"Total Cost : ₹{cost:,}")
    print(f"Exp Return : {ret:.1f} %")
    print(f"Risk Score : {risk}")

    if args.plot:
        plot_frontier(assets, args.capital)
        print("Frontier plot saved to frontier.png")


if __name__ == "__main__":
    main()
