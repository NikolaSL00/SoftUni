# Using a nested list comprehension, write a program that reads rows of a square matrix and its elements, separated by a comma and a space ", ". You should find the matrix's diagonals, prints them and their sum in the format:
# "Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
# Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".


# INPUT:
# 3
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9

# OUTPUT:
# Primary diagonal: 1, 5, 9. Sum: 15
# Secondary diagonal: 3, 5, 7. Sum: 15

def read_matrix():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split(", ")]
        matrix.append(row)
    return matrix


matrix = read_matrix()
primary_diagonal_el = []
secondary_diagonal_el = []

for x in range(len(matrix[0])):
    primary_diagonal_el.append(matrix[x][x])
    secondary_diagonal_el.append(matrix[x][len(matrix[0]) - 1 - x])

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal_el))}. Sum: {sum(primary_diagonal_el)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal_el))}. Sum: {sum(secondary_diagonal_el)}")
