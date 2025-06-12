# Hardcoded stock prices (symbol: price per share)
stock_prices = {
    "AAPL": 185.23,
    "GOOGL": 2743.12,
    "MSFT": 325.60,
    "AMZN": 129.98,
    "TSLA": 215.49
}

portfolio = {}
total_investment = 0

print("Welcome to the Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

# User input loop
while True:
    symbol = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if symbol == "DONE":
        break
    if symbol not in stock_prices:
        print("Invalid symbol. Please choose from:", ", ".join(stock_prices.keys()))
        continue
    try:
        quantity = int(input(f"Enter number of shares for {symbol}: "))
        if quantity < 0:
            print("Please enter a non-negative number.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Add to portfolio
    portfolio[symbol] = portfolio.get(symbol, 0) + quantity
    investment = stock_prices[symbol] * quantity
    total_investment += investment

# Display portfolio and total
print("\n--- Portfolio Summary ---")
for symbol, qty in portfolio.items():
    value = stock_prices[symbol] * qty
    print(f"{symbol}: {qty} shares x ${stock_prices[symbol]:.2f} = ${value:.2f}")
print(f"Total Investment: ${total_investment:.2f}")

# Optional: Save to file
save = input("Do you want to save this summary? (yes/no): ").lower()
if save == "yes":
    file_format = input("Choose file format - txt or csv: ").lower()
    filename = f"portfolio_summary.{file_format}"

    if file_format == "txt":
        with open(filename, "w") as file:
            file.write("Stock Portfolio Summary\n")
            for symbol, qty in portfolio.items():
                value = stock_prices[symbol] * qty
                file.write(f"{symbol}: {qty} shares x ${stock_prices[symbol]:.2f} = ${value:.2f}\n")
            file.write(f"Total Investment: ${total_investment:.2f}\n")
    elif file_format == "csv":
        with open(filename, "w") as file:
            file.write("Stock,Quantity,Price per Share,Total Value\n")
            for symbol, qty in portfolio.items():
                value = stock_prices[symbol] * qty
                file.write(f"{symbol},{qty},{stock_prices[symbol]},{value}\n")
            file.write(f"Total Investment,,,{total_investment}\n")
    else:
        print("Unsupported format. Summary not saved.")
    print(f"Summary saved to {filename}")

print("Thank you for using the tracker!")
