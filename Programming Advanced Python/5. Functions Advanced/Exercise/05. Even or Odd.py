# Create a function called even_odd() that can receive a different quantity of numbers and a command at the end. The command can be "even" or "odd". Filter the numbers depending on the command and return them in a list. Submit only the function in the judge system.

# Test Code:
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))

# OUTPUT:
# [2, 4, 6]

# Test Code:
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

# OUTPUT:
# [1, 3, 5, 7, 9]

def even_odd(*args):
    if args[-1] == "even":
        result = list(filter(lambda x: x % 2 == 0, args[:-1]))
    else:
        result = list(filter(lambda x: x % 2 != 0, args[:-1]))
    return result


