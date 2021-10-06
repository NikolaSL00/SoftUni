# This is your first task at your new job. You were tasked to create a list of the stock in a bakery, and you really don't want to fail at you first day at work.
# You will receive a single line containing some food (keys) and quantities (values). They will be separated by a single space (the first element is the key, the second – the value and so on). Create a dictionary with all the keys and values and print it on the console

# INPUT:
# bread 10 butter 4 sugar 9 jam 12

# OUTPUT:
# {'bread': 10, 'butter': 4, 'sugar': 9, 'jam': 12}

data = input().split()
dictionary = {}
for index in range(0, len(data), 2):
    dictionary[data[index]] = int(data[index + 1])

print(dictionary)
