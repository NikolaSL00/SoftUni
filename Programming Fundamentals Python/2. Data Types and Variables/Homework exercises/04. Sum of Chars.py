# Write a program, which sums the ASCII codes of n characters and prints the sum on the console.
# On the first line, you will receive n – the number of lines.
# On the next n lines – you will receive a letter per line.
# Print the total sum in the following format: "The sum equals: {total_sum}".
# Note: n will be in the interval [1…20].


# INPUT:
# 5
# A
# b
# C
# d
# E

# EXPECTED OUTPUT:
# The sum equals: 399


# INPUT:
# 12
# S
# o
# f
# t
# U
# n
# i
# R
# u
# l
# z
# z

# EXPECTED OUTPUT:
# The sum equals: 1263

num_of_lines = int(input())

sum = 0

for ch in range(1, num_of_lines + 1):
    str = input()
    sum += ord(str)
print(f"The sum equals: {sum}")
