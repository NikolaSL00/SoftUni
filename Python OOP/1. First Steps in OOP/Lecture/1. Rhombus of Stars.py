# Create a program that reads a positive integer N as input and prints on the console a rhombus with size n:

# Input:
# 1

# Output:
# *

# Input:
# 3

# Output:
#   *
#  * *
# * * *
#  * *
#   *

def print_line(spaces_count, stars_count):
    line_spaces = ''.join([' '] * spaces_count)
    line_stars = ' '.join(['*'] * stars_count)
    print(line_spaces + line_stars)

def print_rhombus(n):
    for i in range(n):
        spaces = n - 1 - i
        stars = i + 1
        print_line(spaces, stars)

    for i in range(n - 2, -1, -1):
        spaces = n - i - 1
        stars = i + 1
        print_line(spaces, stars)

print_rhombus(int(input()))