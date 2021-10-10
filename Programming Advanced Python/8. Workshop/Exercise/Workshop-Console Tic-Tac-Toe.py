from errors import InvalidPositionError, InvalidSymbol


def is_board_full(board):
    for row in board:
        is_row_full = all([el is not None for el in row])
        if not is_row_full:
            return False
    return True


def player_get_info():
    player1 = input("Player one name: ")
    player2 = input("Player two name: ")
    while True:
        sign1 = input(f"{player1} would you like to play with 'X' or 'O'? ").upper()
        try:
            if sign1 != "X" and sign1 != "O":
                raise InvalidSymbol
        except InvalidSymbol:
            print("Wrong symbol! You should choose between 'X' or 'O', try again!")
            continue
        break

    sign2 = "O" if sign1 == "X" else "O"

    return [(player1, sign1), (player2, sign2)]


def get_player_choose(player, list_with_busy_positions: list):
    while True:
        chosen_position = int(input(f"{player} choose a free position [1-9]: "))
        try:
            if chosen_position < 0 or chosen_position > 9 or chosen_position in list_with_busy_positions:
                raise InvalidPositionError
            break
        except InvalidPositionError:
            print(f"Wrong index or the position is already taken, try again!")
            continue
    list_with_busy_positions.append(chosen_position)
    return chosen_position - 1


def print_indexes_of_board():
    print("This is the numeration of the board:")
    for index in range(1, 10):
        print(" | ", end="")
        if index % 3 == 0:
            print(index, end="")
            print(" | ")
            continue
        print(str(index), end="")


def initialize_board():
    return [[None] * 3 for x in range(3)]


def print_board(board):
    for index in range(1, 10):
        print(" | ", end="")

        if index <= 3:
            if board[0][index - 1] is not None:
                print(board[0][index - 1], end="")
            else:
                print(" ", end="")
        elif index <= 6:
            if board[1][index - 4] is not None:
                print(board[1][index - 4], end="")
            else:
                print(" ", end="")
        else:
            if board[2][index - 7] is not None:
                print(board[2][index - 7], end="")
            else:
                print(" ", end="")

        if index in (3, 6, 9):
            print(" | ")


def mark_the_chosen_index_on_board(choice, sign, board):
    if choice < 3:
        board[0][choice] = sign
    elif choice < 6:
        board[1][choice - 3] = sign
    else:
        board[2][choice - 6] = sign

    print_board(board)


def check_left_down(count_cells, choice, board, sign):
    row = 0
    if 2 < choice <= 5:
        row = 1
        choice -= 3
    elif 5 < choice <= 8:
        row = 2
        choice -= 6

    for _ in range(count_cells + 1):
        if board[row][choice] != sign:
            return False
        row += 1
        choice -= 1
    return True


def check_left_up(count_cells, choice, board, sign):
    row = 0
    if 2 < choice <= 5:
        row = 1
        choice -= 3
    elif 5 < choice <= 8:
        row = 2
        choice -= 6

    for _ in range(count_cells + 1):
        if board[row][choice] != sign:
            return False
        row -= 1
        choice -= 1
    return True


def check_right_up(count_cells, choice, board, sign):
    row = 0
    if 2 < choice <= 5:
        row = 1
        choice -= 3
    elif 5 < choice <= 8:
        row = 2
        choice -= 6

    for _ in range(count_cells + 1):
        if board[row][choice] != sign:
            return False
        row -= 1
        choice += 1
    return True


def check_right_down(count_cells, choice, board, sign):
    row = 0
    if 2 < choice <= 5:
        row = 1
        choice -= 3
    elif 5 < choice <= 8:
        row = 2
        choice -= 6

    for _ in range(count_cells + 1):
        if board[row][choice] != sign:
            return False
        row += 1
        choice += 1
    return True


def check_right(count_cells, choice, board, sign):
    row = 0
    if 2 < choice <= 5:
        row = 1
        choice -= 3
    elif 5 < choice <= 8:
        row = 2
        choice -= 6

    for _ in range(count_cells + 1):
        if board[row][choice] != sign:
            return False
        choice += 1
    return True


def check_left(count_cells, choice, board, sign):
    row = 0
    if 2 < choice <= 5:
        row = 1
        choice -= 3
    elif 5 < choice <= 8:
        row = 2
        choice -= 6

    for _ in range(count_cells + 1):
        if board[row][choice] != sign:
            return False
        choice -= 1
    return True


def check_up(count_cells, choice, board, sign):
    row = 0
    if 2 < choice <= 5:
        row = 1
        choice -= 3
    elif 5 < choice <= 8:
        row = 2
        choice -= 6

    for _ in range(count_cells + 1):
        if board[row][choice] != sign:
            return False
        row -= 1
    return True


def check_down(count_cells, choice, board, sign):
    row = 0
    if 2 < choice <= 5:
        row = 1
        choice -= 3
    elif 5 < choice <= 8:
        row = 2
        choice -= 6

    for _ in range(count_cells + 1):
        if board[row][choice] != sign:
            return False
        row += 1
    return True


def check_win_conditions(choice, sign, player, board):
    if choice == 0:
        # check right*2
        first_check = check_right(2, choice, board, sign)

        # check down*2
        second_check = check_down(2, choice, board, sign)

        # check right_down*2
        third_check = check_right_down(2, choice, board, sign)

        return first_check or second_check or third_check

    elif choice == 1:
        # check down*2
        first_check = check_down(2, choice, board, sign)

        # check left*1 + check right*1
        second_check = check_left(1, choice, board, sign) and check_right(1, choice, board, sign)

        return first_check or second_check

    elif choice == 2:

        # check left*2
        first_check = check_left(2, choice, board, sign)

        # check down*2
        second_check = check_down(2, choice, board, sign)

        # check left-down*2
        third_check = check_left_down(2, choice, board, sign)

        return first_check or second_check or third_check

    elif choice == 3:
        # check up*1 + down*1
        first_check = check_up(1, choice, board, sign) and check_down(1, choice, board, sign)

        # check right * 2
        second_check = check_right(2, choice, board, sign)

        return first_check or second_check

    elif choice == 4:
        # check up*1 + down*1
        first_check = check_up(1, choice, board, sign) and check_down(1, choice, board, sign)

        # check right*1 + left*1
        second_check = check_right(1, choice, board, sign) and check_left(1, choice, board, sign)

        # check up-right*1 + down-left*1
        third_check = check_right_up(1, choice, board, sign) and check_left_down(1, choice, board, sign)

        # check up-left*1 + down-right*1
        forth_check = check_left_up(1, choice, board, sign) and check_right_down(1, choice, board, sign)

        return first_check or second_check or third_check or forth_check

    elif choice == 5:
        # check up*1 + down*1
        first_check = check_up(1, choice, board, sign) and check_down(1, choice, board, sign)

        # check left * 2
        second_check = check_left(2, choice, board, sign)

        return first_check or second_check

    elif choice == 6:
        # check up*2
        first_check = check_up(2, choice, board, sign)

        # check right*2
        second_check = check_right(2, choice, board, sign)

        # check up-right*2
        third_check = check_right_up(2, choice, board, sign)

        return first_check or second_check or third_check

    elif choice == 7:
        # check up*2
        first_check = check_up(2, choice, board, sign)

        # check left*1 + right*1
        second_check = check_left(1, choice, board, sign) and check_right(1, choice, board, sign)

        return first_check or second_check

    elif choice == 8:
        # check left*2
        first_check = check_left(2, choice, board, sign)

        # check up*2
        second_check = check_up(2, choice, board, sign)

        # check left-up*2
        third_check = check_left_up(2, choice, board, sign)

        return first_check or second_check or third_check


def play(board):
    player1_sign1, player2_sign2 = player_get_info()
    player1, sign1 = player1_sign1
    player2, sign2 = player2_sign2
    print_indexes_of_board()
    print(f"{player1} starts first!")

    list_with_busy_positions = []

    winner_flag = False
    not_winner_board_is_full_flag = False

    while True:
        position_pl1 = get_player_choose(player1, list_with_busy_positions)
        mark_the_chosen_index_on_board(position_pl1, sign1, board)

        winner_flag = check_win_conditions(position_pl1, sign1, player1, board)

        if winner_flag:
            break

        not_winner_board_is_full_flag = is_board_full(board)

        if not_winner_board_is_full_flag:
            break

        player1, player2 = player2, player1
        sign1, sign2 = sign2, sign1

    if winner_flag:
        print(f"{player1} won!")
    else:
        print("Board is full and there is no winner!")


board = initialize_board()
play(board)
