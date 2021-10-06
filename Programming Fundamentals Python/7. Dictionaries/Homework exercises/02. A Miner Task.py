# You will be given sequences of strings, each on a new line, until you receive the command "stop". Every odd line on the console is representing a resource (e.g. Gold, Silver, Copper, and so on) and every even - quantity. Your task is to collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:
# {resource} -> {quantity}
# The quantities will be in the range [1 … 2 000 000 000]

# INPUT:
# Gold
# 155
# Silver
# 10
# Copper
# 17
# stop

# OUTPUT:
# Gold -> 155
# Silver -> 10
# Copper -> 17

# INPUT:
# gold
# 155
# silver
# 10
# copper
# 17
# gold
# 15
# stop

# OUTPUT:
# gold -> 170
# silver -> 10
# copper -> 17

dictionary = {}
command = input()

while command != "stop":
    if command not in dictionary:
        value = int(input())
        dictionary[command] = value
    else:
        value = int(input())
        dictionary[command] += value

    command = input()

for key, value in dictionary.items():
    print(f"{key} -> {value}")
