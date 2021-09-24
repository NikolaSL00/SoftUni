# Write a program, which will take a list of names and print only the unique names in the list.
# The order in which we print the result does not matter.

# INPUT:
# 8
# Lee
# Joey
# Lee
# Joe
# Alan
# Alan
# Peter
# Joey

# OUTPUT:
# Alan
# Joey
# Lee
# Joe
# Peter


# INPUT:
# 7
# Lyle
# Bruce
# Alice
# Easton
# Shawn
# Alice
# Shawn

# OUTPUT:
# Easton
# Lyle
# Alice
# Bruce
# Shawn


# INPUT:
# 6
# Adam
# Adam
# Adam
# Adam
# Adam
# Adam

# OUTPUT:
# Adam

number_of_names = int(input())

set_with_names = {input() for _ in range(number_of_names)}

for name in set_with_names:
    print(name)
