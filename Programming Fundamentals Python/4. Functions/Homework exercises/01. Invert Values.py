# Write a program which receives a single string containing numbers separated by a single space.
# Print a list containing the opposite of each number.


# INPUT:
# 1 2 -3 -3 5

# EXPECTED OUTPUT:
# [-1, -2, 3, 3, -5]


# INPUT:
# -4 0 2 57 -101

# EXPECTED OUTPUT:
# [4, 0, -2, -57, 101]

input_list = []

string = input()

input_list = string.split(" ")

result_list = []
for n in input_list:
    if int(n) < 0:
        value = abs(int(n))
        result_list.append(value)
    else:
        v = -1 * int(n)
        result_list.append(value)
print(result_list)
