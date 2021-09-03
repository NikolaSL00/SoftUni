# You will receive a single number n. On the next n lines you will receive names of courses.
# You should create a list of courses and print it.

# INPUT:
# 2
# PB Python
# PF Python

# EXPECTED OUTPUT:
# ['PB Python', 'PF Python']


# INPUT:
# 4
# Front-End
# C# Web
# JS Core
# Programming Fundamentals

# EXPECTED OUTPUT:
# ['Front-End', 'C# Web', 'JS Core', 'Programming Fundamentals']

n = int(input())
list = []
for row in range(0, n):
    current_course = input()
    list.append(current_course)
print(list)
