# Write a program that receives a matrix of numbers and prints a new one only with the numbers that are even. Use nested comprehension for that problem.
# On the first line, you will receive the rows of the matrix. On the next rows, you will get elements for each column separated with a comma and a space ", ".

# INPUT:
# 2
# 1, 2, 3
# 4, 5, 6

# OUTPUT:
# [[2], [4, 6]]


# INPUT:
# 4
# 10, 33, 24, 5, 1
# 67, 34, 11, 110, 3
# 4, 12, 33, 63, 21
# 557, 45, 23, 55, 67

# OUTPUT:
# [[10, 24], [34, 110], [4, 12], []]


def read_matrix():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split(", ")]
        matrix.append(row)
    return matrix


matrix = read_matrix()

even_matrix = []
for row in matrix:
    even_numbers = [x for x in row if x % 2 == 0]
    even_matrix.append(even_numbers)
print(even_matrix)