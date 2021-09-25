# Write a program that keeps all the unique chemical elements.
# On the first line you will be given a number n - the count of input lines that you are going to receive.
# On the next n lines, you will be receiving chemical compounds, separated by a single space.
# Your task is to print all the unique ones on separate lines (the order does not matter):

# INPUT:
# 4
# Ce O
# Mo O Ce
# Ee
# Mo

# OUTPUT:
# Ce
# Ee
# Mo
# O


# INPUT:
# 3
# Ge Ch O Ne
# Nb Mo Tc
# O Ne

# OUTPUT:
# Ch
# Ge
# Mo
# Nb
# Ne
# O
# Tc

number_of_input_lines = int(input())

set_of_ch_elements = set()

for _ in range(number_of_input_lines):
    input_elements = input().split()
    for el in input_elements:
        set_of_ch_elements.add(el)

for el in set_of_ch_elements:
    print(el)
