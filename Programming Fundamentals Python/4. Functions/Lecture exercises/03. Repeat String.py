# Write a function which receives a string and a counter n.
# The function should return a new string – the result of repeating the old string n times.
# Print the result of the function. Try using lambda.

# INPUT:
# abc
# 3

# EXPECTED OUTPUT:
# abcabcabc


# INPUT:
# String
# 2

# EXPECTED OUTPUT:
# StringString

def repeat_string(string, n):
    return string * n


text = input()
n = int(input())

print(repeat_string(text, n))
