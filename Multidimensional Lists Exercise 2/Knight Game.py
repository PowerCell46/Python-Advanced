def current_knight_func(row, column):
    counter = 0
    if row - 2 > -1 and column - 1 > -1:
        if chess_board[row - 2][column - 1] == "K":
            counter += 1

    if row - 2 > -1 and column + 1 < len(chess_board[0]):
        if chess_board[row - 2][column + 1] == "K":
            counter += 1

    if row - 1 > -1 and column - 2 > -1:
        if chess_board[row - 1][column - 2] == "K":
            counter += 1

    if row + 1 < len(chess_board) and column + 2 < len(chess_board[0]):
        if chess_board[row + 1][column + 2] == "K":
            counter += 1

    if row - 1 > -1 and column + 2 < len(chess_board[0]):
        if chess_board[row - 1][column + 2] == "K":
            counter += 1

    if row + 1 < len(chess_board) and column - 2 > -1:
        if chess_board[row + 1][column - 2] == "K":
            counter += 1

    if row + 2 < len(chess_board) and column + 1 < len(chess_board[0]):
        if chess_board[row + 2][column + 1] == "K":
            counter += 1

    if row + 2 < len(chess_board) and column - 1 > -1:
        if chess_board[row + 2][column - 1] == "K":
            counter += 1

    knight_positions[row, column] = counter


size_of_the_board = int(input())
chess_board = [[el for el in input()] for _ in range(size_of_the_board)]
number_of_removed_knights = 0

while True:
    knight_positions = {}
    for i in range(len(chess_board)):
        current_row = chess_board[i]
        for index in range(len(current_row)):
            if current_row[index] == "K":
                knight_positions[i, index] = 0

    for knight in knight_positions.keys():
        knight_row = knight[0]
        knight_column = knight[1]
        current_knight_func(knight_row, knight_column)
    sorted_tuples_of_knights = (sorted(knight_positions.items(), key=lambda x: -x[1]))

    list_of_results = (list(knight_positions.values()))
    set_of_results = set(list_of_results)
    if len(set_of_results) == 1:
        break
    current_biggest_threat = sorted_tuples_of_knights[0][1]
    for key, value in knight_positions.items():
        if current_biggest_threat == value:
            delete_row = int(key[0])
            delete_column = int(key[1])
            chess_board[delete_row][delete_column] = 0
            number_of_removed_knights += 1
            break

print(number_of_removed_knights)
