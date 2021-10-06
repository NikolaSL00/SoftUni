# You are provided with the following code:
# 
# This code raises many exceptions. Fix it, so it works correctly.

# INPUT:
# 1, 4, 5
# 4, 5, 6, 1, 3
# 2, 5, 10

# OUTPUT:
# 20
# 10
# 1

numbers_list = [int(x) for x in input().split(", ")]

result = 1
for i in range(len(numbers_list)):
    number = numbers_list[i]
    if number <= 5:
        result *= number
    elif number <= 10:
        result /= number
print(result)
