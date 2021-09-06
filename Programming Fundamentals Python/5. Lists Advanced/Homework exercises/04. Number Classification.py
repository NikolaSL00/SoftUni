# Using a list comprehension, write a program that receives numbers, separated by comma and space ", ",
# and prints all the positive, negative, even, and odd numbers on separate lines as shown below.

# Note: Zero is counted for a positive number

# INPUT:
# 1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33

# EXPECTED OUTPUT:
# Positive: 1, 0, 5, 3, 4, 12, 19
# Negative: -2, -100, -20, -33
# Even: -2, 0, 4, -100, -20, 12
# Odd: 1, 5, 3, 19, -33


numbers = [int(el) for el in input().split(", ")]

positive = [el for el in numbers if el >= 0]
negative = [el for el in numbers if el < 0]
even = [el for el in numbers if el % 2 == 0]
odd = [el for el in numbers if not el % 2 == 0]

print(f"Positive: ", end="")
print(", ".join([str(el) for el in positive]), end="")

print(f"\nNegative: ", end="")
print(", ".join([str(el) for el in negative]), end="")

print(f"\nEven: ", end="")
print(", ".join([str(el) for el in even]), end="")

print(f"\nOdd: ", end="")
print(", ".join([str(el) for el in odd]), end="")
