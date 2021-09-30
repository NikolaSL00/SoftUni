# You will be given a square matrix of integers, each integer separated by a single space, and each row will be on a new line. On the last line of input, you will receive indexes - coordinates of several cells separated by a single space, in the following format: "{row1},{column1} {row2},{column2} … {row3},{column3}".
# On those cells there are bombs. You must detonate every bomb, in the order they were given. When a bomb explodes, it deals damage equal to its own integer value, to all the cells around it (in every direction and in all diagonals). One bomb can't explode more than once and after it does, its value becomes 0. When a cell's value reaches 0 or below, it dies. Dead cells can't explode.
# You must print the count of all alive cells and their sum. Afterwards, print the matrix with all its cells (including the dead ones).
# Input
# ⦁	On the first line, you are given the integer N - the size of the square matrix.
# ⦁	The next N lines holds the values of each column - N numbers separated by a space.
# ⦁	On the last line, you will receive the coordinates of the cells with the bombs in the format described above.
# Output
# ⦁	On the first line, you need to print the count of all alive cells in the format:
# "Alive cells: {alive_cells}"
# ⦁	On the second line, you need to print the sum of all alive cell in the format:
# "Sum: {sum_of_cells}"
# ⦁	In the end print the matrix. The cells must be separated by a single space.
# Constraints
# ⦁	The size of the matrix will be between [0…1000].
# ⦁	The bomb coordinates will always be in the matrix.
# ⦁	The bomb's values will always be greater than 0.
# ⦁	The integers of the matrix will be in range [1…10000].


# INPUT:
# 4
# 8 3 2 5
# 6 4 7 9
# 9 9 3 6
# 6 8 1 2
# 1,2 2,1 2,0

# OUTPUT:
# Alive cells: 3
# Sum: 12
# 8 -4 -5 -2
# -3 -3 0 2
# 0 0 -4 -1
# -3 -1 -1 2

# INPUT:
# 3
# 7 8 4
# 3 1 5
# 6 4 9
# 0,2 1,0 2,2

# OUTPUT:
# Alive cells: 3
# Sum: 8
# 4 1 0
# 0 -3 -8
# 3 -8 0
from collections import deque


def is_in_matrix(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols


def do_damage(bomb_coords, matrix, rows, cols):
    r = bomb_coords[0]
    c = bomb_coords[1]
    bomb_damage = matrix[bomb_coords[0]][bomb_coords[1]]

    if is_in_matrix(r - 1, c, rows, cols) and matrix[r - 1][c] > 0:
        matrix[r - 1][c] -= bomb_damage
        # if matrix[r - 1][c] < 0:
        #     matrix[r - 1][c] = 0

    if is_in_matrix(r - 1, c - 1, rows, cols) and matrix[r - 1][c - 1] > 0:
        matrix[r - 1][c - 1] -= bomb_damage
        # if matrix[r - 1][c - 1] < 0:
        #     matrix[r - 1][c - 1] = 0

    if is_in_matrix(r - 1, c + 1, rows, cols) and matrix[r - 1][c + 1] > 0:
        matrix[r - 1][c + 1] -= bomb_damage
        # if matrix[r - 1][c + 1] < 0:
        #     matrix[r - 1][c + 1] = 0

    if is_in_matrix(r + 1, c, rows, cols) and matrix[r + 1][c] > 0:
        matrix[r + 1][c] -= bomb_damage
        # if matrix[r + 1][c] < 0:
        #     matrix[r + 1][c] = 0

    if is_in_matrix(r + 1, c - 1, rows, cols) and matrix[r + 1][c - 1] > 0:
        matrix[r + 1][c - 1] -= bomb_damage
        # if matrix[r + 1][c - 1] < 0:
        #     matrix[r + 1][c - 1] = 0

    if is_in_matrix(r + 1, c + 1, rows, cols) and matrix[r + 1][c + 1] > 0:
        matrix[r + 1][c + 1] -= bomb_damage
        # if matrix[r + 1][c + 1] < 0:
        #     matrix[r + 1][c + 1] = 0

    if is_in_matrix(r, c, rows, cols) and matrix[r][c] >= 0:
        matrix[r][c] -= bomb_damage
        # if matrix[r][c] < 0:
        matrix[r][c] = 0

    if is_in_matrix(r, c + 1, rows, cols) and matrix[r][c + 1] > 0:
        matrix[r][c + 1] -= bomb_damage
        # if matrix[r][c + 1] < 0:
        #     matrix[r][c + 1] = 0

    if is_in_matrix(r, c - 1, rows, cols) and matrix[r][c - 1] > 0:
        matrix[r][c - 1] -= bomb_damage
        # if matrix[r][c - 1] < 0:
        #     matrix[r][c - 1] = 0


rows = int(input())

matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

cols = len(matrix[0])

bombs_coords_str = input().split(" ")
bombs_coords = deque()
for bomb in bombs_coords_str:
    bombs_coords.append([int(x) for x in bomb.split(',')])

while bombs_coords:
    current_bomb = bombs_coords.popleft()
    if is_in_matrix(current_bomb[0], current_bomb[1], rows, cols):
        do_damage(current_bomb, matrix, rows, cols)

count_alive_cells = 0
sum_of_alive_cells = 0

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] > 0:
            count_alive_cells += 1
            sum_of_alive_cells += matrix[row][col]
print(f"Alive cells: {count_alive_cells}")
print(f"Sum: {sum_of_alive_cells}")

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] > 0:
            count_alive_cells += 1
            sum_of_alive_cells += matrix[row][col]
        print(matrix[row][col], end=" ")

    print()
