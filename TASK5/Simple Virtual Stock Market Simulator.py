# Simple Virtual Stock Market Simulator
# Internship Project - Main Flow Services and Technologies

import random

stocks = {"TATA": 100, "INFY": 150, "HDFC": 200}
portfolio = {"TATA": 0, "INFY": 0, "HDFC": 0}
balance = 1000

print("Welcome to Virtual Stock Market Simulator!")
print("Starting Balance:", balance, "\n")

for day in range(1, 6):
    print("Day", day)
    for stock in stocks:
        change = random.randint(-10, 10)
        stocks[stock] += change
        if stocks[stock] < 10:
            stocks[stock] = 10
        print(stock, "price:", stocks[stock])
    
    buy = input("Enter stock to buy (or skip): ").upper()
    if buy in stocks:
        qty = int(input("Enter quantity to buy: "))
        cost = stocks[buy] * qty
        if cost <= balance:
            balance -= cost
            portfolio[buy] += qty
            print("Bought", qty, buy, "shares")
        else:
            print("Not enough balance!")
    else:
        print("Skipped buying.")
    print("Balance:", balance)
    print("Portfolio:", portfolio)
    print("-" * 30)

print("\nFinal Portfolio Value:")
for stock, qty in portfolio.items():
    print(stock, "=", qty, "shares worth", stocks[stock] * qty)
print("Remaining Balance:", balance)
