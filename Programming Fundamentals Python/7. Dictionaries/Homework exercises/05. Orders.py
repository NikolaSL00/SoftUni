# Write a program that keeps information about products and their prices. Each product has a name, a price and a quantity. If the product doesn't exist yet, add it with its starting quantity.
# If you receive a product, which already exists, increase its quantity by the input quantity and if its price is different, replace the price as well.
# You will receive products' names, prices and quantities on new lines. Until you receive the command "buy", keep adding items. When you do receive the command "buy", print the items with their names and total price of all the products with that name.
# Input
# Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
# The product data is always delimited by a single space.
# Output
# Print information about each product in the following format:
# "{productName} -> {totalPrice}"
# Format the total price to the 2nd digit after the decimal separator.


# INPUT:
# Beer 2.20 100
# IceTea 1.50 50
# NukaCola 3.30 80
# Water 1.00 500
# buy

# OUTPUT:
# Beer -> 220.00
# IceTea -> 75.00
# NukaCola -> 264.00
# Water -> 500.00

# INPUT:
# Beer 2.40 350
# Water 1.25 200
# IceTea 5.20 100
# Beer 1.20 200
# IceTea 0.50 120
# buy

# OUTPUT:
# Beer -> 660.00
# Water -> 250.00
# IceTea -> 110.00

# INPUT:
# CesarSalad 10.20 25
# SuperEnergy 0.80 400
# Beer 1.35 350
# IceCream 1.50 25
# buy

# OUTPUT:
# CesarSalad -> 255.00
# SuperEnergy -> 320.00
# Beer -> 472.50
# IceCream -> 37.50

command = input()
buying_dictionary = {}
while command != "buy":
    prod_name, prod_price, prod_qty = command.split()
    prod_qty = float(prod_qty)
    prod_price = float(prod_price)

    if prod_name in buying_dictionary:
        buying_dictionary[prod_name][1] += prod_qty
        if buying_dictionary[prod_name][0] != prod_price:
            buying_dictionary[prod_name][0] = prod_price
    else:
        buying_dictionary[prod_name] = [prod_price, prod_qty]

    command = input()

for product, value in buying_dictionary.items():
    print(f"{product} -> {value[0] * value[1]:.2f}")
