# You are going to create a game called "Miner".
# First, you will receive the size of a square field in which the miner should move.
# On the second line, you will receive the commands for the miner's movement, separated by a single space. The possible commands are "left", "right", "up" and "down".
# In the end, you will receive each row of the field on a separate line. The possible characters that may appear on the screen are:
# ⦁	* - a regular position on the field
# ⦁	e - the end of the route
# ⦁	c - coal
# ⦁	s - miner
# The miner starts moving from the position "s". He should perform the given commands successively, moving with only one position in the given direction. If the miner has reached the edge of the field and the following command indicates that he has to get out of the area, he must remain in his current position and ignore the command.
# When the miner finds coal, he collects it and replaces it with "*". Keep track of the collected coal. In the end, you should print whether the miner has succeeded in collecting the coal or not and his final position:
# ⦁	If the miner has collected all coal in the field, the program stops, and you should print the message: "You collected all coal! ({row_index}, {col_index})".
# ⦁	If the miner steps at "e", the game is over (the program stops), and you should print the message: "Game over! ({row_index}, {col_index})".
# ⦁	If there are no more commands and none of the above cases had happened, you should print the message: "{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})".
# Input
# ⦁	Field size - an integer number
# ⦁	Commands to move the miner - a sequence of directions, separated by a single whitespace (" ")
# ⦁	The field: some of the following characters ("*", "e", "c ", "s"), separated by a single whitespace (" ")
# Output
# ⦁	There are three types of output as mentioned above.
# Constraints
# ⦁	The field size will be a 32-bit integer in the range [0 … 2 147 483 647]
# ⦁	The field will always have only one "s"


# INPUT:
# 5
# up right right up right
# * * * c *
# * * * e *
# * * c * *
# s * * c *
# * * c * *

# OUTPUT:
# Game over! (1, 3)

# INPUT:
# 4
# up right right right down
# * * * e
# * * c *
# * s * c
# * * * *

# OUTPUT:
# You collected all coal! (2, 3)

# INPUT:
# 6
# left left down right up left left down down down
# * * * * * *
# e * * * c *
# * * c s * *
# * * * * * *
# c * * * c *
# * * c * * *

# OUTPUT:
# 3 pieces of coal left. (5, 0)
from collections import deque


def check_does_remain_on_field(r, c, rows):
    return 0 <= r < rows and 0 <= c < rows


all_coals = 0
collected_coals = 0
rows = int(input())
list_of_commands = deque(input().split())
matrix = []

for row in range(rows):
    line = input().split()

    if "s" in line:
        miner_row = row
        miner_col = line.index("s")
    all_coals += line.count("c")
    matrix.append(line)

matrix[miner_row][miner_col] = "*"

while list_of_commands and collected_coals != all_coals:
    current_command = list_of_commands.popleft()

    if current_command == "up":
        if check_does_remain_on_field(miner_row - 1, miner_col, rows):
            miner_row -= 1
            if matrix[miner_row][miner_col] == "c":
                collected_coals += 1
                matrix[miner_row][miner_col] = "*"
            elif matrix[miner_row][miner_col] == "e":
                print(f"Game over! ({miner_row}, {miner_col})")
                break

    elif current_command == "down":
        if check_does_remain_on_field(miner_row + 1, miner_col, rows):
            miner_row += 1
            if matrix[miner_row][miner_col] == "c":
                collected_coals += 1
                matrix[miner_row][miner_col] = "*"
            elif matrix[miner_row][miner_col] == "e":
                print(f"Game over! ({miner_row}, {miner_col})")
                break
    elif current_command == "right":
        if (check_does_remain_on_field(miner_row, miner_col + 1, rows)):
            miner_col += 1
            if matrix[miner_row][miner_col] == "c":
                collected_coals += 1
                matrix[miner_row][miner_col] = "*"
            elif matrix[miner_row][miner_col] == "e":
                print(f"Game over! ({miner_row}, {miner_col})")
                break
    elif current_command == "left":
        if (check_does_remain_on_field(miner_row, miner_col - 1, rows)):
            miner_col -= 1
            if matrix[miner_row][miner_col] == "c":
                collected_coals += 1
                matrix[miner_row][miner_col] = "*"
            elif matrix[miner_row][miner_col] == "e":
                print(f"Game over! ({miner_row}, {miner_col})")
                break

if all_coals == collected_coals:
    print(f"You collected all coal! ({miner_row}, {miner_col})")
elif matrix[miner_row][miner_col] != "e":
    print(f"{all_coals - collected_coals} pieces of coal left. ({miner_row}, {miner_col})")
