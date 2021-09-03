# Write a program that receives two numbers (factor and count) and creates a list with length
# of the given count and contains only integer numbers that are multiples of the given factor.
# The numbers should be only positive, and they should be arranged in ascending order,
# starting from the smallest multiple number.

# INPUT:
# 2
# 5

# EXPECTED OUTPUT:
# [2, 4, 6, 8, 10]


# INPUT:
# 1
# 10

# EXPECTED OUTPUT:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

factor = int(input())
count = int(input())

result_list = []
for i in range(1, count + 1):
    result_list.append((factor * i))
print(result_list)
