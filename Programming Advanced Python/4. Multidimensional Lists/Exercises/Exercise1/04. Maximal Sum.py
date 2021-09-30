# Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square that has maximal sum of its elements. There will be no case with two of more 3x3 squares with equal maximal sum.
# Input
# ⦁	On the first line, you will receive the rows and columns in format "{rows} {columns}" – integers in range [1, 20]
# ⦁	On the next lines you will receive each row with its columns - integers, separated by a single space
# Output
# ⦁	On the first line print the maximum sum of the elements in the 3x3 square in format "Sum = {sum}"
# ⦁	On the next 3 lines print each element of the found submatrix, separated by a single space

# INPUT:
# 4 5
# 1 5 5 2 4
# 2 1 4 14 3
# 3 7 11 2 8
# 4 8 12 16 4

# OUTPUT:
# Sum = 75
# 1 4 14
# 7 11 2
# 8 12 16

# INPUT:
# 5 6
# 1 0 4 3 1 1
# 1 3 1 3 0 4
# 6 4 1 2 5 6
# 2 2 1 5 4 1
# 3 3 3 6 0 5

# OUTPUT:
# Sum = 34
# 2 5 6
# 5 4 1
# 6	0 5

def read_matrix():
    n, m = [int(x) for x in input().split()]
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix


matrix = read_matrix()
max_sum = 0
best_row = 0
best_col = 0
for row in range(len(matrix) - 2):
    for column in range(len(matrix[0]) - 2):
        sum_of_3x3 = matrix[row][column] + matrix[row + 1][column] + matrix[row + 2][column] + matrix[row][column + 1] + \
                     matrix[row][column + 2] + matrix[row + 1][column + 1] + matrix[row + 1][column + 2] + \
                     matrix[row + 2][
                         column + 1] + matrix[row + 2][column + 2]
        if sum_of_3x3 > max_sum:
            max_sum, best_row, best_col = sum_of_3x3, row, column

print(f"Sum = {max_sum}")
print(matrix[best_row][best_col], matrix[best_row][best_col + 1], matrix[best_row][best_col + 2])
print(matrix[best_row + 1][best_col], matrix[best_row + 1][best_col + 1], matrix[best_row + 1][best_col + 2])
print(matrix[best_row + 2][best_col], matrix[best_row + 2][best_col + 1], matrix[best_row + 2][best_col + 2])
