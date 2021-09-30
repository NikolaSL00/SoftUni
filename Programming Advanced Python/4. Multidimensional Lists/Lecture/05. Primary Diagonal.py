# Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from top left to bottom right). On the first line, you will receive an integer N – the size of a square matrix. The next N lines holds the values for each column - N numbers, separated by a single space.

# INPUT:
# 3
# 11 2 4
# 4 5 6
# 10 8 -12

# OUTPUT:
# 4


# INPUT:
# 3
# 1 2 3
# 4 5 6
# 7 8 9

# OUTPUT:
# 15

def read_matrix():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split(" ")]
        matrix.append(row)
    return matrix


matrix = read_matrix()
sum_of_diagonal = 0
for i in range(len(matrix[0])):
    sum_of_diagonal += matrix[i][i]
print(sum_of_diagonal)
