# The budget was enough to get Ali and her friends to Frankfurt and they have some money left, but their final aim is to go to France, which means that they will need more finances. They’ve decided to make profit by buying items on discount from the Thrift Shop and selling them for a higher price. You must help them.
# Create a program that calculates the profit after buying some items and selling them on a higher price. In order to fulfil that, you are going to need certain data - you will receive a collection of items and a budget in the following format:
# {type->price|type->price|type->price……|type->price}
# {budget}
# The prices for each of the types cannot exceed a certain price, which is given bellow:
# Type	Maximum Price
# Clothes	50.00
# Shoes	35.00
# Accessories	20.50
# If a price for a certain item is higher than the maximum price, don’t buy it. Every time you buy an item, you have to reduce the budget with the value of its price. If you don’t have enough money for it, you can’t buy it. Buy as much items as you can.
# You have to increase the price of each of the items you have successfully bought with 40%. Print the list with the new prices and the profit you will gain from selling the items. They need exactly 150$ for tickets for the train, so if their budget after selling the products is enough – print – "Hello, France!" and if not – "Time to go."
# Input / Constraints
# On the 1st line you are going to receive the items with their prices in the format described above – real numbers in the range [0.00……1000.00]
# On the 2nd line, you are going to be given the budget – a real number in the range [0.0….1000.0]
# Output
# Print the list with the bought item’s new prices, rounded 2 digits after the decimal separator in the following format:
# "{price1} {price2} {price3} {price5} … {priceN}"
# Print the profit, formatted to the second decimal point in the following format:
# "Profit: {profit}"
# If the money for tickets is enough, print: "Hello, France!" and if not – "Time to go."


# INPUT:
# Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60
# 120

# EXPECTED OUTPUT:
# 60.62 35.35 51.13
# Profit: 42.03
# Hello, France!


# INPUT:
# Shoes->41.20|Clothes->20.30|Accessories->40|Shoes->15.60|Shoes->33.30|Clothes->48.60
# 90

# EXPECTED OUTPUT:
# 28.42 21.84 46.62
# Profit: 27.68
# Time to go.


type_price_separated = input().split("|")
budget = float(input())

list_with_buys_fully_separated = []
for buy in type_price_separated:
    string = str(buy)
    list_with_buys_fully_separated.append(string.split("->"))

list_with_validated_prices = []
for buy in list_with_buys_fully_separated:
    if buy[0] == "Clothes":
        if not float(buy[1]) > 50.00:
            list_with_validated_prices.append(buy)
    elif buy[0] == "Shoes":
        if not float(buy[1]) > 35.00:
            list_with_validated_prices.append(buy)
    elif buy[0] == "Accessories":
        if not float(buy[1]) > 20.50:
            list_with_validated_prices.append(buy)

list_with_bought_items = []
for item in list_with_validated_prices:
    if float(item[1]) <= budget:
        budget -= float(item[1])
        list_with_bought_items.append(item)
    else:
        continue
profit = 0
sum_of_new_prices = 0
for item in list_with_bought_items:
    new_price = float(item[1]) * 1.40
    sum_of_new_prices += new_price
    profit += float(item[1]) * 0.40
    print(f"{new_price:.2f}", end=" ")

print()
print(f"Profit: {profit:.2f}")

new_budget = budget + sum_of_new_prices

if new_budget <= 150.00:
    print("Time to go.")
else:
    print("Hello, France!")
