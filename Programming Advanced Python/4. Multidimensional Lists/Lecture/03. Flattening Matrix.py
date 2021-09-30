# Write a program that receives a matrix and prints the flattened version of it (a list with all the values). For example, the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4].
# On the first line, you will receive the number of a matrix's rows. On the next rows, you will get the elements for each column separated with a comma and a space ", ".


# INPUT:
# 2
# 1, 2, 3
# 4, 5, 6

# OUTPUT:
# [1, 2, 3, 4, 5, 6]


# INPUT:
# 3
# 10, 2, 21, 4
# 5, 20, 41, 9
# 6, 2, 4, 99

# OUTPUT:
# [10, 2, 21, 4, 5, 20, 41, 9, 6, 2, 4, 99]

def read_matrix():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split(", ")]
        matrix.append(row)
    return matrix


matrix = read_matrix()

flat_matrix = [x
               for row in matrix
               for x in row]
print(flat_matrix)