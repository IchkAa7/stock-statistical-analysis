"""
Functions used to calculate financial statistics and metrics.
"""
def calculate_daily_returns(data):
    """
    Calculate daily percentage returns from closing prices.
    """
    data = data.copy()

    data["Daily Return"] = data["Close"].pct_change()

    return data


def calculate_return_statistics(data):
    """
    Calculate basic statistics on daily returns.
    """

    returns = data["Daily Return"].dropna()

    mean_return = returns.mean()
    volatility = returns.std()
    best_day = returns.max()
    worst_day = returns.min()

    return {
        "mean_daily_return": mean_return,
        "daily_volatility": volatility,
        "best_day": best_day,
        "worst_day": worst_day
    }