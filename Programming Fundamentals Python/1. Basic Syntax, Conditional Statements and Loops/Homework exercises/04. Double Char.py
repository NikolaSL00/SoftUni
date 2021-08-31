# You will be given a string.
# You should print a string in which each character (case-sensitive) is repeated twice.

# INPUT:
# Hello World

# EXPECTED OUTPUT:
# HHeelllloo  WWoorrlldd


# INPUT:
# 1234!

# EXPECTED OUTPUT:
# 11223344!!

string = input()

for i in range(0, len(string)):
    print(string[i], end="")
    print(string[i], end="")
