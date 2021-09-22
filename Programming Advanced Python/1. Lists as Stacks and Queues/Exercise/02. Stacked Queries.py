# You have an empty stack. You will receive an integer – N.
# On the next N lines you will receive queries.
# Each query is one of these four types:

# '1 {number}' – push the number (integer) into the stack
# '2' – delete the number at the top of the stack
# '3' – print the maximum number in the stack
# '4' – print the minimum number in the stack

# It is guaranteed that each query is valid.
# After you go through all the queries, print the stack from the top to the bottom in the following format:

# "{n}, {n1}, {n2}, ... {nn}"


# INPUT:
# 9
# 1 97
# 2
# 1 20
# 2
# 1 26
# 1 20
# 3
# 1 91
# 4

# OUTPUT:
# 26
# 20
# 91, 20, 26

# INPUT:
# 10
# 2
# 1 47
# 1 66
# 1 32
# 4
# 3
# 1 25
# 1 16
# 1 8
# 4

# OUTPUT:
# 32
# 66
# 8
# 8, 16, 25, 32, 66, 47

number_of_line_with_commands = int(input())
stack = []

for _ in range(number_of_line_with_commands):
    command_parts = input().split()
    command = command_parts[0]

    if command == "1":
        number = int(command_parts[1])
        stack.append(number)
    elif command == "2":
        if stack:
            stack.pop()
    elif command == "3":
        if stack:
            print(max(stack))
    elif command == "4":
        if stack:
            print(min(stack))

reversed_stack = []

while stack:
    el = stack.pop()
    if stack:
        print(el, end=", ")
    else:
        print(el)
