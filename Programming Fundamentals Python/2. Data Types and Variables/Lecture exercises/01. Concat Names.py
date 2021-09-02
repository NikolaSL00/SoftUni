# Write a program which reads two names and a delimiter. It should print the names joined by the delimiter.

# INPUT:
# John
# Smith
# ->

# EXPECTED OUTPUT:
# John->Smith


# INPUT:
# Jan
# White
# <->

# EXPECTED OUTPUT:
# Jan<->White


# INPUT:
# Linda
# Terry
# =>

# EXPECTED OUTPUT:
# Linda=>Terry

name1 = input()
name2 = input()
delimiter = input()

print(f"{name1}{delimiter}{name2}")
