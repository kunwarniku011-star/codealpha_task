import csv
print("==============================")
print("STOCK PORTFOLIO TRACKER")
print("==============================")
# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420
}
# Dictionary to store portfolio records
portfolio = {}
# Input stock details
while True:
    stock_name = input("Enter stock name (AAPL/TSLA/GOOGL/MSFT): ")
    stock_name = stock_name.upper()
    if stock_name not in stock_prices:
        print("Stock not available. Please try again.")
        continue
    quantity = int(input("Enter quantity: "))
    # Get price from dictionary
    price = stock_prices[stock_name]
    # Calculate total stock value
    total_value = quantity * price
    # Store stock details
    portfolio[stock_name] = {
        "quantity": quantity,
        "price": price,
        "total_value": total_value
    }
    print("\nStock Name:", stock_name)
    print("Quantity:", quantity)
    print("Price per Share:", price)
    print("Total Stock Value:", total_value)
    choice = input("Add another stock? (yes/no): ")

    if choice.lower() != "yes":
        break
# Calculate total investment
portfolio_total = 0
for stock_name in portfolio:
    stock_data = portfolio[stock_name]
    portfolio_total += stock_data["total_value"]
# Display portfolio summary
print("\n===== PORTFOLIO SUMMARY =====")
for stock_name in portfolio:
    stock_data = portfolio[stock_name]
    print("\nStock Name:", stock_name)
    print("Quantity:", stock_data["quantity"])
    print("Price per Share:", stock_data["price"])
    print("Total Value:", stock_data["total_value"])
print("\nTotal Investment Value:", portfolio_total)
# Save results to CSV file
with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Stock Name",
        "Quantity",
        "Price",
        "Total Value"
    ])
    for stock_name in portfolio:
        stock_data = portfolio[stock_name]

        writer.writerow([
            stock_name,
            stock_data["quantity"],
            stock_data["price"],
            stock_data["total_value"]
        ])

print("\nPortfolio saved to portfolio.csv")
print("===== THANK YOU =====")