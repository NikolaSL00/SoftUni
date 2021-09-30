# Write a program that reads a matrix from the console and prints the sum for each column on separate lines.
# On the first line, you will get matrix sizes in format "{rows}, {columns}". On the next rows, you will get elements for each column separated with a single space.

# INPUT:
# 3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0

# OUTPUT:
# 12
# 10
# 19
# 20
# 8
# 7


# INPUT:
# 3, 3
# 1 2 3
# 4 5 6
# 7 8 9

# OUTPUT:
# 12
# 15
# 18

def read_matrix():
    n, m = [int(x) for x in input().split(", ")]
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split(" ")]
        matrix.append(row)
    return matrix


matrix = read_matrix()

m = len(matrix[0])

for column in range(m):
    sum_col = 0
    for row in range(len(matrix)):
        sum_col += matrix[row][column]
    print(sum_col)
