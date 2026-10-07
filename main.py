from src.data_loader import load_stock_data


def main():
    data = load_stock_data(
        ticker="AAPL",
        start_date="2020-01-01",
        end_date="2026-01-01"
    )

    print(data.head())


if __name__ == "__main__":
    main()