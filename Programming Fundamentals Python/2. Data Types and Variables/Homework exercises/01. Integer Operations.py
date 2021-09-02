# Write a program which reads four integer numbers.
# It should add the first to the second number,
# integer divide the sum by the third number and multiply the result by the fourth number. Print the final result.

# INPUT:
# 10
# 20
# 3
# 3

# EXPECTED OUTPUT:
# 30


# INPUT:
# 15
# 14
# 2
# 3

# EXPECTED OUTPUT:
# 42

number = int(input())
number1 = int(input())
number2 = int(input())
number3 = int(input())

result = ((number + number1) // number2) * number3

print(result)
