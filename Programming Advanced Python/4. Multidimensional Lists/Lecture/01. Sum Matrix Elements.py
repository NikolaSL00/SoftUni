# Write a program that reads a matrix from the console and prints:
# ⦁	The sum of all numbers in the matrix
# ⦁	The matrix itself
# On the first line, you will receive the matrix sizes in the format "{rows}, {columns}". On the next rows, you will get elements for each column separated by a comma and a space ", ".

# INPUT:
# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0

# OUTPUT:
# 76
# [[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]

def read_matrix():
    n, m = [int(x) for x in input().split(", ")]

    matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(", ")]
        matrix.append(row)
    return matrix

matrix = read_matrix()

sum_of_el = 0
for el in matrix:
    sum_of_el += sum(el)
print(sum_of_el)
print(matrix)
