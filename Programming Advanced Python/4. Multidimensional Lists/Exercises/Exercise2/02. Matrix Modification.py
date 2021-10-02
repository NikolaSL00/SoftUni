# Write a program that reads a matrix from the console and changes its values. On the first line, you will get the matrix's rows - N. You will get elements for each column on the following N lines, separated with a single space. You will be receiving commands in the following format:
# ⦁	"Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
# ⦁	"Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
# If the coordinate is invalid, you should print "Invalid coordinates". A coordinate is valid if both of the given indexes are in range [0; len() – 1].
# When you receive "END", you should print the matrix and stop the program.


# INPUT:
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Add 0 0 5
# Subtract 1 1 2
# END

# OUTPUT:
# 6 2 3
# 4 3 6
# 7 8 9

# INPUT:
# 4
# 1 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 1
# Add 4 4 100
# Add 3 3 100
# Subtract -1 -1 42
# Subtract 0 0 42
# END

# OUTPUT:
# Invalid coordinates
# Invalid coordinates
# -41 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 101

def check_if_indices_are_valid(r, c, rows):
    return 0 <= r < rows and 0 <= c < rows


rows = int(input())

matrix = []

for row in range(rows):
    line = [int(x) for x in input().split()]

    matrix.append(line)

while True:
    command = input()
    if command == "END":
        break
    type_of_command, row_index, col_index, value = command.split()

    if check_if_indices_are_valid(int(row_index), int(col_index), rows):
        pass
    else:
        print("Invalid coordinates")
        continue

    if type_of_command == "Add":
        matrix[int(row_index)][int(col_index)] += int(value)
    elif type_of_command == "Subtract":
        matrix[int(row_index)][int(col_index)] -= int(value)
for row in matrix:
    print(" ".join(map(str, row)))
