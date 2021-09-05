# Write a function which calculates the total price of an order and returns it.
# The function should receive one of the following products: "coffee", "coke", "water" or "snacks",
# and a quantity of the product. The prices for a single piece of each product are:

# ⦁	coffee - 1.50
# ⦁	water - 1.00
# ⦁	coke - 1.40
# ⦁	snacks - 2.00
#
# Print the result formatted to the second decimal place.

# INPUT:
# water
# 5

# EXPECTED OUTPUT:
# 5.00

# INPUT:
# coffee
# 2

# EXPECTED OUTPUT:
# 3.00

def calculate_total_price(product, quantity):
    if product == "water":
        return quantity
    elif product == "coffee":
        return quantity * 1.50
    elif product == "coke":
        return quantity * 1.40
    elif product == "snacks":
        return quantity * 2


product = input()
quantity = int(input())
var = calculate_total_price(product, quantity)
print(f"{var:.2f}")
