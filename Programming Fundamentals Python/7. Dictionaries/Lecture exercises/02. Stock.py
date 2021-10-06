# After you have successfully completed your first task, your boss decides to give you another one right away. Now not only you have to keep track of the stock, but also you should answer customers if you have some products in stock or not.
# You will be given key-value pairs of products and quantities (on a single line separated by space). On the next line you will be given products to search for. Check for each product, you have 2 possibilities:
# ⦁	If you have the product, print "We have {quantity} of {product} left"
# ⦁	Otherwise, print "Sorry, we don't have {product}"


# INPUT:
# cheese 10 bread 5 ham 10 chocolate 3
# jam cheese ham tomatoes

# OUTPUT:
# Sorry, we don't have jam
# We have 10 of cheese left
# We have 10 of ham left
# Sorry, we don't have tomatoes

data = input().split()
searched_products = input().split()
dictionary = {}
for index in range(0, len(data), 2):
    dictionary[data[index]] = int(data[index + 1])

for index in range(0, len(searched_products)):
    if searched_products[index] in dictionary:
        print(f"We have {dictionary[searched_products[index]]} of {searched_products[index]} left")
    else:
        print(f"Sorry, we don't have {searched_products[index]}")
