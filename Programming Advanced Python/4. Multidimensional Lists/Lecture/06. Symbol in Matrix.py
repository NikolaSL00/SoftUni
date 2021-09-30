# Write a program that reads a number - N, representing the rows and columns of a square matrix. On the next N lines, you will receive rows of the matrix. Each row consists of ASCII characters. After that, you will receive a symbol. Find the first occurrence of that symbol in the matrix and print its position in the format: "({row}, {col})". You should start searching from the top left. If there is no such symbol print the message "{symbol} does not occur in the matrix".

# INPUT:
# 3
# ABC
# DEF
# X!@
# !

# OUTPUT:
# (2, 1)


# INPUT:
# 4
# asdd
# xczc
# qwee
# qefw
# 4

# OUTPUT:
# 4 does not occur in the matrix

def read_matrix():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = [x for x in input()]
        matrix.append(row)
    return matrix


matrix = read_matrix()
searched_symbol = input()
flag_found = False

for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if matrix[r][c] == searched_symbol:
            print(f"{r, c}")
            flag_found = True
            break
    if flag_found:
        break
if not flag_found:
    print(f"{searched_symbol} does not occur in the matrix")
