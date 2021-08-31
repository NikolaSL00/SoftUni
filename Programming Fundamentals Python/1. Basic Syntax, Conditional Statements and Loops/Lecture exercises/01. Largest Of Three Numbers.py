# Write a program that receives three whole numbers and print the largest one.

# INPUT:
# 3
# -1
# 5

# EXPECTED OUTPUT:
# 5

# INPUT:
# 0
# -1
# -2

# EXPECTED OUTPUT:
# 0

number1 = int(input())
number2 = int(input())
number3 = int(input())

if number1 >= number2 and number1 >= number3:
    print(number1)
elif number2 >= number1 and number2 >= number3:
    print(number2)
else:
    print(number3)
