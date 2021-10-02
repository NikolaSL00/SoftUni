# Your task is to collect as many eggs as possible for the holiday.
# On the first line, you will be given a number representing the size of the field. On the following few lines, you will be given a field with:
# ⦁	One bunny - randomly placed in it and marked with the symbol "B"
# ⦁	Number of eggs placed at different positions of the field and traps marked with "X"
# Your job is to find out the direction in which the bunny should go in order to collect the maximum number of eggs. The directions that should be considered as possible are up, down, left, and right. If you reach a trap while checking some of the directions, you should not consider the fields after the trap in this direction. For more clarifications, see the examples below.
# Input
# ⦁	A number representing the size of the field
# ⦁	The matrix representing the field (each position separated by a single space)
# Output
# ⦁	The direction which should be considered as best (lowercase)
# ⦁	The field positions from which we are collecting eggs as lists
# ⦁	The total number of eggs collected

# INPUT:
# 5
# 1 3 7 9 11
# X 5 4 X 63
# 7 3 21 95 1
# B 1 73 4 9
# 9 2 33 2 0

# OUTPUT:
# right
# [3, 1]
# [3, 2]
# [3, 3]
# [3, 4]
# 87

# INPUT:
# 8
# 4 18 9 7 24 41 52 11
# 54 21 19 X 6 34 75 57
# 76 67 7 44 76 27 56 37
# 92 35 25 37 52 34 56 72
# 35 X 1 45 4 X 37 63
# 105 X B 2 12 43 5 19
# 48 19 35 20 32 27 42 4
# 73 88 78 32 37 52 X 22

# OUTPUT:
# down
# [6, 2]
# [7, 2]
# 113
def if_in_matrix(r, c, row):
    return 0 <= r < row and 0 <= c < row


def make_a_walk(bunny_row, bunny_col, matrix):
    next_position_row = bunny_row - 1
    next_position_column = bunny_col
    path_of_cells_up = []
    # up
    while if_in_matrix(next_position_row, next_position_column, len(matrix)):
        if matrix[next_position_row][next_position_column] == "X":

            break
        else:
            path_of_cells_up.append([next_position_row,next_position_column])
        next_position_row -= 1

    # down
    next_position_row = bunny_row + 1
    next_position_column = bunny_col
    path_of_cells_down = []
    while if_in_matrix(next_position_row, next_position_column, len(matrix)):
        if matrix[next_position_row][next_position_column] == "X":

            break
        else:
            path_of_cells_down.append([next_position_row,next_position_column])
        next_position_row += 1

    # right
    next_position_row = bunny_row
    next_position_column = bunny_col + 1
    path_of_cells_right = []
    while if_in_matrix(next_position_row, next_position_column, len(matrix)):
        if matrix[next_position_row][next_position_column] == "X":

            break
        else:
            path_of_cells_right.append([next_position_row,next_position_column])
        next_position_column += 1

    # left
    next_position_row = bunny_row
    next_position_column = bunny_col - 1
    path_of_cells_left = []
    while if_in_matrix(next_position_row, next_position_column, len(matrix)):
        if matrix[next_position_row][next_position_column] == "X":

            break
        else:
            path_of_cells_left.append([next_position_row,next_position_column])
        next_position_column -= 1

    return path_of_cells_left, path_of_cells_right, path_of_cells_up, path_of_cells_down


def sum_path_elements_and_return_result(matrix, path1, path2, path3, path4):
    result_path1 = 0
    direction = ""
    for elemenents in path1:
        result_path1 += int(matrix[elemenents[0]][elemenents[1]])

    result_path2 = 0
    for elemenents in path2:
        result_path2 += int(matrix[elemenents[0]][elemenents[1]])

    result_path3 = 0
    for elemenents in path3:
        result_path3 += int(matrix[elemenents[0]][elemenents[1]])

    result_path4 = 0
    for elemenents in path4:
        result_path4 += int(matrix[elemenents[0]][elemenents[1]])

    return max((result_path1, path1, "left"), (result_path2, path2, "right"), (result_path3, path3, "up"),
               (result_path4, path4, "down"))


field_size = int(input())
matrix = []

bunny_row_coords = -5
bunny_column_coords = -5

for row in range(field_size):
    line = [x for x in input().split()]
    if "B" in line:
        bunny_row_coords = row
        bunny_column_coords = line.index("B")
    matrix.append(line)

path1, path2, path3, path4 = make_a_walk(bunny_row_coords, bunny_column_coords, matrix)
result = sum_path_elements_and_return_result(matrix, path1, path2, path3, path4)

print(result[2])
for el in result[1]:
    print(el)
print(result[0])