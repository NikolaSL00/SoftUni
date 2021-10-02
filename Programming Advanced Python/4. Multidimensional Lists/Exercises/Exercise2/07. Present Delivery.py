# The presents are ready, and Santa has to deliver them to the kids.
# You will receive an integer m for the number of presents Santa has and an integer n for the size of the neighborhood with a square shape. On the following lines, you will receive the matrix, which represents the neighborhood.
# Santa will be in a random cell, marked with the letter "S". Each cell stands for a house where children may live. If the cell has "X" on it, that means there lives a naughty kid. Otherwise, if a nice kid lives there, the cell is marked by "V". There can also be cells marked with "C" for cookies. All of the empty positions will be marked with "-".
# Santa can move "up", "down", "left", "right" with one position each time. These will be the commands that you receive. If he moves to a house with a nice kid, the kid receives a present, but if Santa reaches a house with a naughty kid, he doesn't drop a present. If the command sends Santa to a cell marked with "C", Santa eats cookies and becomes happy and extra generous to all the kids around him* (meaning all of them will receive presents - it doesn't matter if naughty or nice). If Santa has been to a house, the cell becomes "-".
# Note: *around him means on his left, right, upwards, and downwards by one cell. In this case, Santa doesn't move to these cells, or if he does, he returns to the cell where the cookie was.
# If Santa runs out of presents or receives the command "Christmas morning", you should end the program.
# Keep in mind that you should check whether all the nice kids received presents.
# Input
# ⦁	On the first line, you are given the integer m - the count of presents
# ⦁	On the second - integer n - the size of the neighborhood
# ⦁	The following n lines hold the values for every row
# ⦁	On each of the following lines you will get a command
# Output
# ⦁	On the first line:
# ⦁	If Santa runs out of presents, but there are still some nice kids left print: "Santa ran out of presents!"
# ⦁	Next, print the matrix.
# ⦁	In the end, print one of these messages:
# ⦁	If he manages to give all the nice kids presents, print:
# "Good job, Santa! {count_nice_kids} happy nice kid/s."
# ⦁	Otherwise, print:
# "No presents for {count nice kids} nice kid/s."
# Constraints
# ⦁	The size of the square matrix will be between [2…10].
# ⦁	Santa’s position will be marked with 'S'.
# ⦁	There will always be at least 1 nice kid.
# ⦁	There won't be a case where the cookie is on the border of the matrix.


# INPUT:
# 5
# 4
# - X V -
# - S - V
# - - - -
# X - - -
# up
# right
# down
# right
# Christmas morning

# OUTPUT:
# - - - -
# - - - S
# - - - -
# X - - -
# Good job, Santa! 2 happy nice kid/s.

# INPUT:
# 3
# 4
# - - - -
# V - X -
# - V C V
# - - - S
# left
# up

# OUTPUT:
# Santa ran out of presents!
# - - - -
# V - - -
# - - S -
# - - - -
# No presents for 1 nice kid/s.

def get_next_position(r, c, direction):
    if direction == "right":
        return r, c + 1
    if direction == "left":
        return r, c - 1
    if direction == "up":
        return r - 1, c
    if direction == "down":
        return r + 1, c


def if_in_matrix(r, c, size):
    return 0 <= r < size and 0 <= c < size


presents_count = int(input())

size_of_neighborhood = int(input())
santa_row, santa_col = -1, -1
matrix = []

nice_kids = []

for row in range(size_of_neighborhood):
    line = [x for x in input().split()]
    if "S" in line:
        santa_row = row
        santa_col = line.index("S")

    if "V" in line:
        for column in range(size_of_neighborhood):
            if line[column] == "V":
                nice_kids.append([row, column])

    matrix.append(line)


def look_around(row, col, matrix, presents_count: int, nice_kids: list):
    # matrix[row][col - 1]
    # matrix[row][col + 1]
    # matrix[row - 1][col]
    # matrix[row + 1][col]
    if presents_count > 0 and if_in_matrix(row, col - 1, len(matrix)):
        if matrix[row][col - 1] == "V":
            presents_count -= 1
            matrix[row][col - 1] = "-"
            nice_kids.remove([row, col - 1])

        if matrix[row][col - 1] == "X":
            presents_count -= 1
            matrix[row][col - 1] = "-"

    if presents_count > 0 and if_in_matrix(row, col + 1, len(matrix)):
        if matrix[row][col + 1] == "V":
            presents_count -= 1
            matrix[row][col + 1] = "-"
            nice_kids.remove([row, col + 1])

        if matrix[row][col + 1] == "X":
            presents_count -= 1
            matrix[row][col + 1] = "-"

    if presents_count > 0 and if_in_matrix(row - 1, col, len(matrix)):
        if matrix[row - 1][col] == "V":
            presents_count -= 1
            matrix[row - 1][col] = "-"
            nice_kids.remove([row - 1, col])

        if matrix[row - 1][col] == "X":
            presents_count -= 1
            matrix[row - 1][col] = "-"

    if presents_count > 0 and if_in_matrix(row + 1, col, len(matrix)):
        if matrix[row + 1][col] == "V":
            presents_count -= 1
            matrix[row + 1][col] = "-"
            nice_kids.remove([row + 1, col])

        if matrix[row + 1][col] == "X":
            presents_count -= 1
            matrix[row + 1][col] = "-"
    return presents_count


all_nice_kids = len(nice_kids)

while True:
    if presents_count <= 0:
        break
    command = input()
    if command == "Christmas morning":
        break
    current_row, current_col = get_next_position(santa_row, santa_col, command)

    if if_in_matrix(current_row, current_col, size_of_neighborhood):
        matrix[santa_row][santa_col] = "-"
        el = matrix[current_row][current_col]
        if el == "X":
            matrix[current_row][current_col] = "-"
            santa_row, santa_col = current_row, current_col
            matrix[santa_row][santa_col] = "S"

        elif el == "V":
            presents_count -= 1
            matrix[current_row][current_col] = "-"
            nice_kids.remove([current_row, current_col])
            santa_row, santa_col = current_row, current_col
            matrix[santa_row][santa_col] = "S"

        elif el == "C":
            matrix[current_row][current_col] = "-"
            presents_count = look_around(current_row, current_col, matrix, presents_count, nice_kids)
            santa_row, santa_col = current_row, current_col
            matrix[santa_row][santa_col] = "S"

        else:
            santa_row, santa_col = current_row, current_col
            matrix[santa_row][santa_col] = "S"

if presents_count <= 0 and nice_kids:
    print("Santa ran out of presents!")

for row in matrix:
    print(' '.join(row))

if nice_kids:
    print(f"No presents for {len(nice_kids)} nice kid/s.")
else:
    print(f"Good job, Santa! {all_nice_kids} happy nice kid/s.")
