# Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
# On the first line, you will receive an integer N - the size of a square matrix. The next N lines holds the values for each column - N numbers separated by a single space. Print the absolute difference between the sums of the primary and the secondary diagonal.

# INPUT:
# 3
# 11 2 4
# 4 5 6
# 10 8 -12

# OUTPUT:
# 15

# INPUT:
# 4
# -7 14 9 -20
# 3 4 9 21
# -14 6 8 44
# 30 9 7 -14

# OUTPUT:
# 34

def read_matrix():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix


matrix = read_matrix()

primary_diagonal_el = 0
secondary_diagonal_el = 0

for x in range(len(matrix[0])):
    primary_diagonal_el += matrix[x][x]
    secondary_diagonal_el += matrix[x][len(matrix[0]) - 1 - x]

print(abs(primary_diagonal_el - secondary_diagonal_el))
