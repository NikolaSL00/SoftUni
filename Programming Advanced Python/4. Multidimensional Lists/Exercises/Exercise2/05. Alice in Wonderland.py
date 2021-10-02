# Alice is going to the mad tea party, to see her friends. On the way to the party she needs to collect bags of tea.
# You will be given an integer n for the size of the Wonderland territory with a square shape. On the following n lines, you will receive the rows of the territory:
# ⦁	Alice will be placed in a random position, marked with the letter "A".
# ⦁	On the territory there will be bags of tea, represented as numbers. If Alice steps on a number position, she collects the tea bags and increases the quantity with the corresponding number.
# ⦁	There will always be one rabbit hole on the territory marked with the letter "R".
# ⦁	All of the empty positions will be marked with ".".
# After the field state, you will be given commands for Alice's movements. Move commands can be: "up", "down", "left" or "right".
# When Alice collects at least 10 bags of tea, she is ready to go to the tea party, and she does not need to continue collecting. Otherwise, if she steps on the rabbit hole or goes out of the territory, she can't return, and the program ends.
# It the end, all the path she walked has to be marked with '*'.
# For more clarifications, see the examples below.
# Input
# ⦁	On the first line, you will be given the integer n – the size of the square matrix
# ⦁	On the following n lines - matrix representing the field (each position separated by a single space)
# ⦁	On each of the following lines you will be given a move command
# Output
# ⦁	On the first line:
# ⦁	If Alice steps on the rabbit hole or she go out of the territory, print:
# "Alice didn't make it to the tea party."
# ⦁	If she collected at least 10 bags of tea, print:
# "She did it! She went to the party."
# ⦁	On the following lines, print the matrix.
# Constraints
# ⦁	Alice will always either go outside the Wonderland or collect 10 bags of tea
# ⦁	All the commands will be valid
# ⦁	All of the given numbers will be valid integers in the range [0, 10]

# INPUT:
# 5
# . A . . 1
# R . 2 . .
# 4 7 . 1 .
# . . . 2 .
# . 3 . . .
# down
# right
# left
# down
# up
# left

# OUTPUT:
# Alice didn't make it to the tea party.
# . * . . 1
# * * * . .
# 4 * . 1 .
# . . . 2 .
# . 3 . . .

# INPUT:
# 7
# . A . 1 1 . .
# 9 . . . 6 . 5
# . 6 . R . . .
# . 3 . . 1 . .
# . . . 2 . . 2
# . 3 . . 1 . .
# . 8 3 . . . 2
# left
# down
# down
# right

# OUTPUT:
# She did it! She went to the party.
# * * . 1 1 . .
# * . . . 6 . 5
# * * . R . . .
# . 3 . . 1 . .
# . . . 2 . . 2
# . 3 . . 1 . .
# . 8 3 . . . 2
def if_in_matrix(r, c, row):
    return 0 <= r < row and 0 <= c < row


def get_next_position(direction, r, c):
    if direction == "up":
        return r - 1, c
    elif direction == "down":
        return r + 1, c
    elif direction == "left":
        return r, c - 1
    elif direction == "right":
        return r, c + 1


size = int(input())

matrix = []
alice_row, alice_col = 0, 0

for row in range(size):
    elements = input().split()
    matrix.append(elements)
    for col in range(size):
        element = elements[col]
        if element == "A":
            alice_row, alice_col = row, col

matrix[alice_row][alice_col] = "*"

tea_bags = 0
while True:
    command = input()
    alice_row, alice_col = get_next_position(command, alice_row, alice_col)
    if not if_in_matrix(alice_row, alice_col, size):
        break
    cell_value = matrix[alice_row][alice_col]
    matrix[alice_row][alice_col] = "*"
    if cell_value == "R":
        break
    if cell_value.isdigit():
        tea_bags += int(cell_value)
        if tea_bags >= 10:
            break

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
for row in matrix:
    print(' '.join(row))
