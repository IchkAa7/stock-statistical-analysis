from src.data_loader import load_stock_data
from src.metrics import calculate_daily_returns, calculate_return_statistics


def main():
    data = load_stock_data(
        ticker="AAPL",
        start_date="2020-01-01",
        end_date="2026-01-01"
    )

    data = calculate_daily_returns(data)

    stats = calculate_return_statistics(data)

    print("\nRETURN STATISTICS")
    print(f"Mean daily return: {stats['mean_daily_return']:.4%}")
    print(f"Daily volatility: {stats['daily_volatility']:.4%}")
    print(f"Best day: {stats['best_day']:.4%}")
    print(f"Worst day: {stats['worst_day']:.4%}")


if __name__ == "__main__":
    main()