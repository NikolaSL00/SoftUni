# Write a program to flatten several lists of numbers received in the following format:
# ⦁	String with numbers or empty strings separated by "|"
# ⦁	Values are separated by spaces (" ", one or several)
# ⦁	Order the output list from the last to the first matrix sub-lists and their values from left to right as shown below

# INPUT:
# 1 2 3 |4 5 6 |  7  88

# OUTPUT:
# 7 88 4 5 6 1 2 3

# INPUT:
# 7 | 4  5|1 0| 2 5 |3

# OUTPUT:
# 3 2 5 1 0 4 5 7

# INPUT:
# 1| 4 5 6 7  |  8 9

# OUTPUT:
# 8 9 4 5 6 7 1

line = input().split("|")
stack = []

while line:
    el = line.pop()
    stack.append([int(x) for x in el.split()])

for elements in stack:
    for sub_elements in elements:
        print(sub_elements, end=" ")
