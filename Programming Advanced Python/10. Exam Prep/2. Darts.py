def is_strike_in_matrix(matrix, r, c):
    return (r >= 0 and r < len(matrix)) and (c >= 0 and c < len(matrix[0]))


def cases_with_different_points(matrix, row, col):
    el = matrix[row][col]
    if el.isdigit():
        return int(el)
    elif el == "D":
        return get_number_from_borders(col, matrix, row) * 2
    elif el == "T":
        return get_number_from_borders(col, matrix, row) * 3
    elif el == "B":
        return 501


def get_number_from_borders(col, matrix, row):
    left = int(matrix[row][0])
    right = int(matrix[row][-1])
    up = int(matrix[0][col])
    down = int(matrix[-1][col])
    return down + left + right + up


def turn(player: str, matrix, row, col):
    if is_strike_in_matrix(matrix, row, col):
        result = cases_with_different_points(matrix, row, col)
        dictionary[player] -= result
        if dictionary[player] <= 0:
            return "winner"


name1, name2 = input().split(", ")
dictionary = {
    name1: 501,
    name2: 501
}
turn_counter_dict = {
    name1: 0,
    name2: 0
}
matrix = []

for _ in range(7):
    line = input().split()
    matrix.append(line)

turn_respond = None

while turn_respond != "winner":
    coords = input().split(", ")
    row = int(coords[0][1:])
    col = int(coords[1][:-1])
    turn_respond = turn(name1, matrix, row, col)
    turn_counter_dict[name1] += 1
    name1, name2 = name2, name1

print(f"{name2} won the game with {turn_counter_dict[name2]} throws!")
