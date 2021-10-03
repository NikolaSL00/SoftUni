# Write a function called concatenate() that receives some strings, concatenates them, and returns the result.

# Test Code:
# print(concatenate("Soft", "Uni", "Is", "Great", "!"))

# OUTPUT:
# SoftUniIsGreat!

# Test Code:
# print(concatenate("I", " ", "Love", " ", "Python"))

# OUTPUT:
# I Love Python

def concatenate(*args):
    result = ""
    for el in args:
        result += el
    return result
