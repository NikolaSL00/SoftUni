# You are participating in a Firearm course. It is a training day at the shooting range.
# You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented as some symbols separated by a single space:
# ⦁	Your position is marked with the symbol "A"
# ⦁	Targets marked with symbol "x"
# ⦁	All of the empty positions will be marked with "."
# After the field state, you will be given an integer representing the number of commands you will receive. The possible commands are:
# ⦁	"move {right/left/up/down} {steps}" – you should move in the given direction with the given steps. You can only move if the field you want to step on is marked with ".".
# ⦁	"shoot {right/left/up/down}" – you should shoot in the given direction (from your current position without moving). Beware that there might be targets that stand in the way of other targets, and you cannot reach them - you can shoot only the nearest target. When you have shot a target, the field becomes empty position (".").
# Validate the positions since they can be outside the field.
# Keep track of all the shot targets:
# ⦁	If at any point there are no targets left, end the program and print: "Training completed! All {count_targets} targets hit.".
# ⦁	If, after you perform all the commands, there are some targets left print: "Training not completed! {count_left_targets} targets left.".
# Finally, print the index positions of the targets that you hit, as shown in the examples.
# Input
# ⦁	5 lines representing the field (symbols, separated by a single space)
# ⦁	N - count of commands
# ⦁	On the following N lines - the commands in the format described above
# Output
# ⦁	On the first line, print one of the following:
# ⦁	If all the targets were shot
# "Training completed! All {count_targets} targets hit."
# ⦁	Otherwise:
#               	       "Training not completed! {count_left_targets} targets left."
# ⦁	Finally, print the index positions "[{row}, {column}]" of the targets that you hit, as shown in the examples.
# Constrains
# ⦁	All the commands will be valid
# ⦁	There will always be at least one target

# INPUT:
# . . . . .
# x . . . .
# . A . . .
# . . . x .
# . x . . x
# 3
# shoot down
# move right 4
# move left 1

# OUTPUT:
# Training not completed! 3 targets left.
# [4, 1]

# INPUT:
# . . . . .
# . . . . .
# . A x . .
# . . . . .
# . x . . .
# 2
# shoot down
# shoot right

# OUTPUT:
# Training completed! All 2 targets hit.
# [4, 1]
# [2, 2]

# INPUT:
# . . . . .
# . . . . .
# . . x . .
# . . . . .
# . x . . A
# 3
# shoot down
# move right 2
# shoot left

# OUTPUT:
# Training not completed! 1 targets left.
# [4, 1]

def if_in_matrix(r, c, size):
    return 0 <= r < size and 0 <= c < size


def shoot_direction(shot_targets, targets_list: list, direction, pos_row, pos_col, matrix):
    if direction == "right":
        for cells in range(pos_col + 1, 5):
            if [pos_row, cells] in targets_list:
                matrix[pos_row][cells] = "."
                shot_targets.append([pos_row, cells])
                targets_list.remove(shot_targets[-1])
                break

    elif direction == "left":

        for cells in range(pos_col - 1, -1, -1):
            if [pos_row, cells] in targets_list:
                matrix[pos_row][cells] = "."
                shot_targets.append([pos_row, cells])
                targets_list.remove(shot_targets[-1])
                break

    elif direction == "up":

        for cells in range(pos_row - 1, -1, -1):
            if [cells, pos_col] in targets_list:
                matrix[cells][pos_col] = "."
                shot_targets.append([cells, pos_col])
                targets_list.remove(shot_targets[-1])
                break

    elif direction == "down":

        for cells in range(pos_row + 1, 5):
            if [cells, pos_col] in targets_list:
                matrix[cells][pos_col] = "."
                shot_targets.append([cells, pos_col])
                targets_list.remove(shot_targets[-1])
                break


def move_get_next_coords(r, c, direction, steps):
    if direction == "right":
        return r, c + steps

    elif direction == "left":
        return r, c - steps

    elif direction == "up":
        return r - steps, c

    elif direction == "down":
        return r + steps, c


matrix = []
pos_row, pos_col = 0, 0
shot_targets = []
targets = []

for row in range(5):
    line = [x for x in input().split()]
    if "A" in line:
        pos_row = row
        pos_col = line.index("A")
    if "x" in line:
        for column in range(5):
            if line[column] == "x":
                targets.append([row, column])
    matrix.append(line)

number_of_commands = int(input())

matrix[pos_row][pos_col] = "."

for _ in range(number_of_commands):
    command = input().split()
    direction = command[1]

    if command[0] == "move":
        steps = int(command[2])
        current_row, current_col = move_get_next_coords(pos_row, pos_col, direction, steps)
        if if_in_matrix(current_row, current_col, 5):
            if matrix[current_row][current_col] != ".":
                continue
            else:
                pos_row, pos_col = current_row, current_col

        else:
            continue

    elif command[0] == "shoot":
        shoot_direction(shot_targets, targets, direction, pos_row, pos_col, matrix)

if targets:
    print(f"Training not completed! {len(targets)} targets left.")
    if shot_targets:
        for el in shot_targets:
            print(el)
else:
    print(f"Training completed! All {len(shot_targets)} targets hit.")
    if shot_targets:
        for el in shot_targets:
            print(el)
