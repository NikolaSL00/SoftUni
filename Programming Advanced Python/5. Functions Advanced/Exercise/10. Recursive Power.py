# Create a recursive function called recursive_power() which should receive a number and a power. Using recursion, return the result of number ** power. Submit only the function in the judge system.

# Test Code:
# print(recursive_power(2, 10))

# OUTPUT:
# 1024

# Test Code:
# print(recursive_power(10, 100))

# OUTPUT:
# 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

def recursive_power(base, exponent):
    if exponent == 1:
        return base
    return recursive_power(base, exponent - 1) * base

