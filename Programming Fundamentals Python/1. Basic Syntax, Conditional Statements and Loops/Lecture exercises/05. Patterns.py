# Write a program which receives a number and creates the following pattern.
# The number represents the largest count of stars on one row.

# INPUT:
# 3

# EXPECTED OUTPUT:
# *
# **
# ***
# **
# *

# INPUT:
# 5

# EXPECTED OUTPUT:
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

number = int(input())

rows = number * 2 - 1
comparison = 0

for i in range(0, rows):
    print("")
    comparison += 1
    n = 1
    if i == number:
        break
    while n <= comparison:
        print("*", end="")
        n += 1

comparison = number

for i in range(rows, 0, -1):
    comparison -= 1
    n = comparison
    for x in range(0, comparison):
        print("*", end="")
    print("")
