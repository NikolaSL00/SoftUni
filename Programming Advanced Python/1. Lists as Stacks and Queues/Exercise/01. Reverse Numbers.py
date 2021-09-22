# Write a program which reads from the console a string with N integers,
# separated by a single space, and reverses them using a stack.
# Print the reversed integers on one line, separated by a single space.

# INPUT:
# 1 2 3 4 5

# OUTPUT:
# 5 4 3 2 1

# INPUT:
# 1

# OUTPUT:
# 1


numbers_as_stack = input().split(" ")

result = []

while numbers_as_stack:
    result.append(numbers_as_stack.pop())
print(" ".join(result))
