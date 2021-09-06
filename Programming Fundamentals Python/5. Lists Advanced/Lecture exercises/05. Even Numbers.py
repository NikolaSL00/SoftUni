# Write a program that reads a single string with numbers separated by comma and space ", ".
# Print the indices of all even numbers.

# INPUT:
# 3, 2, 1, 5, 8

# EXPECTED OUTPUT:
# [1, 4]


# INPUT:
# 2, 4, 6, 9, 10

# EXPECTED OUTPUT:
# [0, 1, 2, 4]

list_of_numbers = [int(el) for el in input().split(", ")]

print([index for index in range(len(list_of_numbers)) if list_of_numbers[index] % 2 == 0])
