def points_per_gift(total_points):
    if 100 <= total_points <= 199:
        print(f"Good job! You scored {total_points} points, and you've won Football.")
    elif 200 <= total_points <= 299:
        print(f"Good job! You scored {total_points} points, and you've won Teddy Bear.")
    elif 300 <= total_points:
        print(f"Good job! You scored {total_points} points, and you've won Lego Construction Set.")
    else:
        print(f"Sorry! You need {100 - total_points} points more to win a prize.")


def if_coords_in_matrix(row, col):
    return 0 <= row < 6 and 0 <= col < 6


def get_points_from_column(col, matrix):
    points = 0
    for row in range(len(matrix)):
        for index in range(len(matrix[0])):
            if index == col:
                if matrix[row][col].isdigit():
                    points += int(matrix[row][col])
    return points


matrix = []

points_total = 0

striked_bucket_coordinates = []

for _ in range(6):
    line = input().split()
    matrix.append(line)

for _ in range(3):
    strike_coordinates = input().split(", ")
    row = int(strike_coordinates[0][1:])
    col = int(strike_coordinates[1][:-1])

    if if_coords_in_matrix(row, col):
        el = matrix[row][col]
        if el == "B":
            if (row, col) not in striked_bucket_coordinates:
                points_total += get_points_from_column(col, matrix)
                striked_bucket_coordinates.append((row, col))

points_per_gift(points_total)
