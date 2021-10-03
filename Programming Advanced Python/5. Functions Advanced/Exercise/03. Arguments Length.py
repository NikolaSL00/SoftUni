# Create a function called args_length() that returns the number of the arguments. Submit only the function in the judge system.

# Test Code:
# print(args_length(1, 32, 5))

# OUTPUT:
# 3

# Test Code:
# print(args_length("john", "peter"))

# OUTPUT:
# 2

# Test Code:
# print(args_length([1, 2, 3]))

# OUTPUT:
# 1

def args_length(*args):
    return len(args)