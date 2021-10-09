def is_player_choice_valid(player_choice, board):
    is_column_valid = 0 <= player_choice <= len(board[0])
    if is_column_valid:
        has_column_space = board[0][player_choice] is None
    else:
        return False
    return is_column_valid and has_column_space


def get_player_choice(player):
    choice = input(f"Player {player}, please choose a column.\n")
    return int(choice) - 1


def apply_player_choice(board, player_choice, player):
    row_index = 0
    while row_index < len(board) and board[row_index][player_choice] is None:
        row_index += 1

    board[row_index - 1][player_choice] = player
    return row_index - 1


def check_win_conditions(board, row, column):
    player = board[row][column]
    found_winner = False
    # checking conditions for up_winning_condtion is not necessary, because it will never be true, while we keep adding the numbers on top, but if necessary there is the code:

    # # up
    # # row -1
    # current_row = row
    # for _ in range(3):
    #     if current_row - 1 >= 0 and board[current_row - 1][column] == player:
    #         current_row -= 1
    #         found_winner = True
    #     else:
    #         found_winner = False
    #         break
    #
    # if found_winner:
    #     return f"The winner is player {player}"

    # check up_right
    # row - 1, column + 1
    current_row = row
    current_column = column
    for _ in range(3):
        if current_row - 1 >= 0 and current_column + 1 < len(board[0]) and board[current_row - 1][
            current_column + 1] == player:
            current_row -= 1
            current_column += 1
            found_winner = True
        else:
            found_winner = False
            break
    if found_winner:
        return f"The winner is player {player}"

    # check up_left
    # row - 1, column - 1
    current_row = row
    current_column = column
    for _ in range(3):
        if current_row - 1 >= 0 and current_column - 1 >= 0 and board[current_row - 1][
            current_column - 1] == player:
            current_row -= 1
            current_column -= 1
            found_winner = True
        else:
            found_winner = False
            break
    if found_winner:
        return f"The winner is player {player}"

    # check right
    current_column = column
    for _ in range(3):
        if current_column + 1 < len(board[0]) and board[row][current_column + 1] == player:
            current_column += 1
            found_winner = True
        else:
            found_winner = False
            break

    if found_winner:
        return f"The winner is player {player}"

    # check down_right
    # row + 1, column + 1
    current_row = row
    current_column = column
    for _ in range(3):
        if current_row + 1 < len(board) and current_column + 1 > len(board[0]) and board[current_row + 1][
            current_column + 1] == player:
            current_row += 1
            current_column += 1
            found_winner = True
        else:
            found_winner = False
            break
    if found_winner:
        return f"The winner is player {player}"

    # check down
    # row + 1
    current_row = row
    for _ in range(3):
        if current_row + 1 < len(board) and board[current_row + 1][column] == player:
            current_row += 1
            found_winner = True
        else:
            found_winner = False
            break

    if found_winner:
        return f"The winner is player {player}"

    # check down_left
    # row + 1, column - 1
    current_column = column
    current_row = row
    for _ in range(3):
        if current_row + 1 < len(board) and current_column - 1 >= 0 and board[current_row + 1][
            current_column - 1] == player:

            current_column -= 1
            current_row += 1
            found_winner = True
        else:
            found_winner = False
            break
    if found_winner:
        return f"The winner is player {player}"

    # check left
    current_column = column
    for _ in range(3):
        if current_column - 1 >= 0 and board[row][current_column - 1] == player:
            current_column -= 1
            found_winner = True
        else:
            found_winner = False
            break

    if found_winner:
        return f"The winner is player {player}"


def play(board):
    current_player, other_player = 1, 2
    while True:
        player_choice = get_player_choice(current_player)
        if not is_player_choice_valid(player_choice, board):
            print("Wrong column, try again!")
            continue
        print(player_choice)
        current_row = apply_player_choice(board, player_choice, current_player)
        print_board(board)
        result = check_win_conditions(board, current_row, player_choice)
        if result is not None:
            print(result)
            break
        current_player, other_player = other_player, current_player


def create_board(rows_count, column_count):
    return [[None] * column_count for _ in range(rows_count)]


def print_board(board):
    for row in board:
        print([x if x is not None else 0 for x in row])


board = create_board(6, 7)
play(board)
# new_board = [
#     [1],
#     [1],
#     [1],
#     [1],
#     [1],
#     [1],
# ]
# print_board(new_board)
# print(check_win_conditions(new_board, 3, 0))
