# Write a function which receives three integer numbers and returns the smallest.
# Print the result on the console. Use appropriate name for the function.

# INPUT:
# 2
# 5
# 3

# EXPECTED OUTPUT:
# 2


# INPUT:
# 600
# 342
# 123

# EXPECTED OUTPUT:
# 123

def smallest_integer(num_1, num_2, num_3):
    min_number = num_1
    if min_number > num_2:
        min_number = num_2
    if min_number > num_3:
        min_number = num_3
    return min_number


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

min_number = smallest_integer(number_1, number_3, number_2)

print(min_number)
