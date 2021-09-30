# Find the number of all 2x2 squares containing identical chars in a matrix. On the first line, you will receive the matrix's dimensions in format "{rows} {columns}". On the next rows you will receive characters, separated by a single space. Print the number of all square matrices you have found.

# INPUT:
# 3 4
# A B B D
# E B B B
# I J B B

# OUTPUT:
# 2

# INPUT:
# 2 2
# a b
# c d

# OUTPUT:
# 0

# INPUT:
# 5 4
# A A B D
# A A B B
# I J B B
# C C C G
# C C K P

# OUTPUT:
# 3

def read_matrix():
    n, m = [int(x) for x in input().split()]
    matrix = []
    for _ in range(n):
        row = [x for x in input().split()]
        matrix.append(row)
    return matrix


matrix = read_matrix()
count = 0

for index_row in range(len(matrix) - 1):
    for index_column in range(len(matrix[0]) - 1):
        if matrix[index_row][index_column] == matrix[index_row][index_column + 1] and \
                matrix[index_row + 1][index_column] == matrix[index_row + 1][index_column + 1] and \
                matrix[index_row][index_column + 1] == matrix[index_row + 1][index_column + 1]:
            count += 1
print(count)