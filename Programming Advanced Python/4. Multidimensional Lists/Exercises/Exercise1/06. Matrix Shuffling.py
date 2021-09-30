# Write a program that reads a matrix, from the console and perform certain operations with its elements. User input is provided in a similar way like in the problems above - first you read the dimensions and then the data.
# Your program should receive commands in the format: "swap {row1} {col1} {row2} {col2}" where ("row1", "col1") and ("row2", "col2") are the coordinates of two points in the matrix. A valid command starts with the "swap" keyword along with four valid coordinates (no more, no less), separated by a single space.
# ⦁	If the command is valid, you should swap the values at the given indexes and print the matrix at each step (thus you will be able to check if the operation was performed correctly).
# ⦁	If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered or the given coordinates are not valid), print "Invalid input!" and move on to the next command. A negative value makes the coordinates not valid.
# Your program should finish when the command "END" is entered.


# INPUT:
# 2 3
# 1 2 3
# 4 5 6
# swap 0 0 1 1
# swap 10 9 8 7
# swap 0 1 1 0
# END

# OUTPUT:
# 5 2 3
# 4 1 6
# Invalid input!
# 5 4 3
# 2 1 6

# INPUT:
# 1 2
# Hello World
# 0 0 0 1
# swap 0 0 0 1
# swap 0 1 0 0
# END

# OUTPUT:
# Invalid input!
# World Hello
# Hello World

def check_is_valid(row, col, matrix):
    if 0 <= col <= len(matrix[0]):
        if 0 <= row <= len(matrix):
            return True
    return False


def swap_values_in_matrix(row1, col1, row2, col2, matrix):
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]


rows, columns = [int(x) for x in input().split()]

matrix = []

for row in range(rows):
    matrix.append(input().split())

while True:
    command = input()
    if command == "END":
        break
    command_params = command.split()

    if command_params[0] != "swap" or len(command_params) != 5:
        print("Invalid input!")
        continue

    if not (check_is_valid(int(command_params[1]), int(command_params[2]), matrix)) or \
            not (check_is_valid(int(command_params[3]), int(command_params[4]), matrix)):
        print("Invalid input!")
        continue
    else:
        swap_values_in_matrix(int(command_params[1]), int(command_params[2]), int(command_params[3]),
                              int(command_params[4]), matrix)
        for row in matrix:
            print(' '.join(map(str, row)))
