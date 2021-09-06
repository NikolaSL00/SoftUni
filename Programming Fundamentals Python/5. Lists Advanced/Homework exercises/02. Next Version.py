# You are fed up with changing the version of your software manually.
# Instead, you will create a little script that will make it for you.
# You will be given a string representing the version of your software in the format: "{n1}.{n2}.{n3}".
# Your task is to print the next version. For example, if the current version is "1.3.4", the next version will be
# "1.3.5".
# The only rule is that the numbers cannot be greater than 9. If it happens,
# set the current number to 0 and increase the previous number. For more clarification, see the examples below.
# Note: there will be no case in which the first number will become greater than 9.

# INPUT:
# 1.2.3

# EXPECTED OUTPUT:
# 1.2.4


# INPUT:
# 3.9.9

# EXPECTED OUTPUT:
# 4.0.0


current_version = [int(el) for el in input().split(".")]

next_version = current_version

if next_version[2] < 9:
    next_version[2] += 1
elif next_version[1] < 9:
    next_version[1] += 1
    next_version[2] = 0
elif next_version[0] < 9:
    next_version[0] += 1
    next_version[1] = 0
    next_version[2] = 0

print(".".join([str(el) for el in next_version]))
