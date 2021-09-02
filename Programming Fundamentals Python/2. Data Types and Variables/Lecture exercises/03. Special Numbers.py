# A number is special when the sum of its digits is 5, 7 or 11. Write a program which reads an integer n.
# Then, for all numbers in the range 1…n, prints the number and if it is special or not (True / False).

# INPUT:
# 15

# EXPECTED OUTPUT:
# 1 -> False
# 2 -> False
# 3 -> False
# 4 -> False
# 5 -> True
# 6 -> False
# 7 -> True
# 8 -> False
# 9 -> False
# 10 -> False
# 11 -> False
# 12 -> False
# 13 -> False
# 14 -> True
# 15 -> False


number = int(input())

for num in range(1, number + 1):
    num_as_string = str(num)
    result = 0
    for el in num_as_string:
        result += int(el)
    if result == 5 or result == 7 or result == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
