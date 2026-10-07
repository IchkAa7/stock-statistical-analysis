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
import numpy as np


def calculate_cumulative_return(data):
    returns = data["Daily Return"].dropna()

    cumulative_return = (1 + returns).prod() - 1

    return cumulative_return


def calculate_annualized_return(data):
    returns = data["Daily Return"].dropna()

    cumulative_growth = (1 + returns).prod()
    number_of_days = len(returns)

    annualized_return = cumulative_growth ** (252 / number_of_days) - 1

    return annualized_return


def calculate_annualized_volatility(data):
    returns = data["Daily Return"].dropna()

    daily_volatility = returns.std()

    annualized_volatility = daily_volatility * np.sqrt(252)

    return annualized_volatility


def calculate_max_drawdown(data):
    close = data["Close"].squeeze()

    running_max = close.cummax()

    drawdown = (close - running_max) / running_max

    max_drawdown = drawdown.min()

    return max_drawdown