# You seem to be doing great at your first job. You have now successfully completed the first 2 of your tasks and your boss decides to give you as your next task something more challenging. You have to accept all the new products coming in the bakery and finally gather some statistics.
# You will be receiving key-value pairs on separate lines separated by ": " until you receive the command "statistics". Sometimes you may receive a product more than once. In that case you have to add the new quantity to the existing one. When you receive the "statistics" command, print the following:
# "Products in stock:
# - {product1}: {quantity1}
# - {product2}: {quantity2}
# …
# Total Products: {count_all_products}
# Total Quantity: {sum_all_quantities}"

# INPUT:
# bread: 4
# cheese: 2
# ham: 1
# bread: 1
# statistics

# OUTPUT:
# Products in stock:
# - bread: 5
# - cheese: 2
# - ham: 1
# Total Products: 3
# Total Quantity: 8

command = input()
dictionary = dict()

while command != "statistics":

    key, value = command.split(": ")
    if key in dictionary:
        dictionary[key] += int(value)
    else:
        dictionary[key] = int(value)
    command = input()

print("Products in stock:")
for key, value in dictionary.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(dictionary.keys())}")
print(f"Total Quantity: {sum(dictionary.values())}")
