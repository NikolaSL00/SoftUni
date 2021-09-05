# Write a function that receives two integer numbers. Calculate factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.

# INPUT:
# 5
# 2

# EXPECTED OUTPUT:
# 60.00


# INPUT:
# 6
# 2

# EXPECTED OUTPUT:
# 360.00

# Write a function that receives two integer numbers. Calculate factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.

def factorials_division(num1, num2):
    factorial1 = 1
    factorial2 = 1
    for i in range(num1, 0, -1):
        factorial1 *= i
    for i in range(num2, 0, -1):
        factorial2 *= i
    return factorial1 / factorial2


number_1 = int(input())
number_2 = int(input())
result = factorials_division(number_1, number_2)
print(f"{result:.2f}")
