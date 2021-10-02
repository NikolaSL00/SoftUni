# Chess is the oldest game, but it is still popular these days. For this task, we will use only one chess piece - the Knight.
# A chess knight has 8 possible moves it can make, as illustrated. It can move to the nearest square but not on the same row, column, or diagonal. (e.g., it can move two squares horizontally, then one square vertically, or it can move one square horizontally then two squares vertically - i.e., in an "L" pattern.) 
# The knight game is played on a board with dimensions N x N.
# You will receive a board with "K" for knights and "0" for empty cells. Your task is to remove knights until there are no knights left that can attack one another.
#
# Input
# ⦁	On the first line, you will receive integer N - the size of the board
# ⦁	On the following N lines, you will receive strings with "K" and "0"
# Output
# ⦁	Print a single integer with the minimum number of knights that need to be removed
# Constraints
# ⦁	The size of the board will be 0 < N < 30
# ⦁	Time limit: 0.3 sec. Memory limit: 16 MB


# INPUT:
# 5
# 0K0K0
# K000K
# 00K00
# K000K
# 0K0K0

# OUTPUT:
# 1

# INPUT:
# 2
# KK
# KK

# OUTPUT:
# 0

# INPUT:
# 8
# 0K0KKK00
# 0K00KKKK
# 00K0000K
# KKKKKK0K
# K0K0000K
# KK00000K
# 00K0K000
# 000K00KK

# OUTPUT:
# 12

def initialize_horses(dict_of_horses: dict):
    for key, value in dict_of_horses.items():
        dict_of_horses[key] = 0
    return dict_of_horses


def is_in_matrix(r, c, rows):
    return 0 <= r < rows and 0 <= c < rows


def check_if_can_kill_other(coordinates_of_the_horse, matrix, dict_with_knight):
    # 8 possible positions
    row = coordinates_of_the_horse[0]
    col = coordinates_of_the_horse[1]

    if is_in_matrix(row - 2, col - 1, len(matrix)) and (row - 2, col - 1) in dict_with_knight:
        dict_with_knight[(row - 2, col - 1)] += 1
    if is_in_matrix(row - 2, col + 1, len(matrix)) and (row - 2, col + 1) in dict_with_knight:
        dict_with_knight[(row - 2, col + 1)] += 1
    if is_in_matrix(row - 1, col - 2, len(matrix)) and (row - 1, col - 2) in dict_with_knight:
        dict_with_knight[(row - 1, col - 2)] += 1
    if is_in_matrix(row + 1, col - 2, len(matrix)) and (row + 1, col - 2) in dict_with_knight:
        dict_with_knight[(row + 1, col - 2)] += 1
    if is_in_matrix(row + 1, col + 2, len(matrix)) and (row + 1, col + 2) in dict_with_knight:
        dict_with_knight[(row + 1, col + 2)] += 1
    if is_in_matrix(row - 1, col + 2, len(matrix)) and (row - 1, col + 2) in dict_with_knight:
        dict_with_knight[(row - 1, col + 2)] += 1
    if is_in_matrix(row + 2, col - 1, len(matrix)) and (row + 2, col - 1) in dict_with_knight:
        dict_with_knight[(row + 2, col - 1)] += 1
    if is_in_matrix(row + 2, col + 1, len(matrix)) and (row + 2, col + 1) in dict_with_knight:
        dict_with_knight[(row + 2, col + 1)] += 1


dict_with_knight = dict()
size_of_board = int(input())
matrix = []
list_with_horses = []
count_of_removed = 0
flag_remove = True

for row in range(size_of_board):
    line = [x for x in input()]
    for column_index in range(len(line)):
        if line[column_index] == "K":
            list_with_horses.append([row, column_index])
            dict_with_knight[(row, column_index)] = 0
    matrix.append(line)

while flag_remove:
    flag_remove = False
    max_value = -1
    key_of_max_value = None

    dict_with_knight = initialize_horses(dict_with_knight)

    for knight in list_with_horses:
        check_if_can_kill_other(knight, matrix, dict_with_knight)

    for key, value in dict_with_knight.items():
        if value > 0:
            flag_remove = True
        if max_value < value:
            key_of_max_value = key
            max_value = value
    if flag_remove:
        dict_with_knight.pop(key_of_max_value)
        count_of_removed += 1
        list_with_horses.remove([key_of_max_value[0], key_of_max_value[1]])

print(count_of_removed)
