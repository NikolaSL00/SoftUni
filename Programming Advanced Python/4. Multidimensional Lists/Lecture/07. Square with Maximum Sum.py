# Write a program that reads a matrix from the console and finds the 2x2 top-left submatrix with biggest sum of its values.
# On first line you will get matrix sizes in format "{rows}, {columns}".  On the next rows, you will get elements for each column, separated with a comma and a space ", ".
# You should print the found submatrix and the sum of its elements as shown in the examples.


# INPUT:
# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0

# OUTPUT:
# 9 8
# 7 9
# 33


# INPUT:
# 2, 4
# 10, 11, 12, 13
# 14, 15, 16, 17

# OUTPUT:
# 12 13
# 16 17
# 58

def read_matrix():
    n, m = [int(x) for x in input().split(", ")]
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split(", ")]
        matrix.append(row)
    return matrix


matrix = read_matrix()

starting_row = 0
stating_column = 0

max_sum_of_square = 0
squares = []

for row in range(len(matrix)):
    for column in range(len(matrix[0])):
        sum = 0
        if row + 1 < len(matrix) and column + 1 < len(matrix[0]):
            sum += matrix[row][column]
            sum += matrix[row + 1][column + 1]
            sum += matrix[row + 1][column]
            sum += matrix[row][column + 1]

        if sum > max_sum_of_square:
            max_sum_of_square = sum
            squares.clear()
            squares.append(matrix[row][column])
            squares.append(matrix[row][column+1])
            squares.append(matrix[row+1][column])
            squares.append(matrix[row + 1][column + 1])

print(squares[0], squares[1])
print(squares[2], squares[3])
print(max_sum_of_square)
