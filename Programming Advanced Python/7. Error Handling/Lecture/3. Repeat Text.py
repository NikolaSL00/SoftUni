# Write a program that receives text on the first line and times (to repeat the text) that must be an integer. If the user passes non-integer type for the times variable, handle the exception and print a message
# "Variable times must be an integer".


# INPUT:
# Hello
# Bye

# OUTPUT:
# Variable times must be an integer

# INPUT:
# Hello
# 2

# OUTPUT:
# HelloHello

try:
    text = input()
    times = int(input())
    print(text * times)
except ValueError:
    print("Variable times must be an integer")
