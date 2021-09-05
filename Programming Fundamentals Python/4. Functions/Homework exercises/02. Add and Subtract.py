# You will receive three integer numbers.
# Write functions named:
# sum_numbers() which returns the sum of the first two integers
# subtract() which returns the difference between the returned result of the first function and the third integer.
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.
# Print the result of the subtract() function on the console.


# INPUT:
# 23
# 6
# 10

# EXPECTED OUTPUT:
# 19


# INPUT:
# 1
# 17
# 30

# EXPECTED OUTPUT:
# -12

def sum_numbers(n_1, n_2):
    return n_1 + n_2


def subtract(result, n_3):
    return result - n_3


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

result = subtract(sum_numbers(num_1, num_2), num_3)
print(result)
