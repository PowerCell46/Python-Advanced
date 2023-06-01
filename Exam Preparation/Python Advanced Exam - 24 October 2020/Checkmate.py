chess_board = [[el for el in input().split(" ")] for row in range(8)]
queens_locations = []
for i in range(8):
    for j in range(8):
        if chess_board[i][j] == "Q":
            queens_locations.append([i, j])


def queen_attack(current_row, current_position):
    # right
    for position in range(current_position + 1, 8):
        if chess_board[current_row][position] == "K":
            return True
        elif chess_board[current_row][position] == "Q":
            break
    # left
    for position in range(current_position - 1, -1, -1):
        if chess_board[current_row][position] == "K":
            return True
        elif chess_board[current_row][position] == "Q":
            break
    # top
    for row in range(current_row - 1, -1, -1):
        if chess_board[row][current_position] == "K":
            return True
        elif chess_board[row][current_position] == "Q":
            break
    # bottom
    for row in range(current_row + 1, 8):
        if chess_board[row][current_position] == "K":
            return True
        elif chess_board[row][current_position] == "Q":
            break
    # upper left diagonal
    for index in range(1, 8):
        row = current_row - index
        position = current_position - index
        if row < 0 or position < 0:
            break
        if chess_board[row][position] == "K":
            return True
        elif chess_board[row][position] == "Q":
            break
    # right lower diagonal
    for index in range(1, 8):
        row = current_row + index
        position = current_position + index
        if row == 8 or position == 8:
            break
        if chess_board[row][position] == "K":
            return True
        elif chess_board[row][position] == "Q":
            break
    # upper right diagonal
    for index in range(1, 8):
        row = current_row - index
        position = current_position + index
        if row < 0 or position == 8:
            break
        if chess_board[row][position] == "K":
            return True
        elif chess_board[row][position] == "Q":
            break
    # left lower diagonal
    for index in range(1, 8):
        row = current_row + index
        position = current_position - index
        if row == 8 or position < 0:
            break
        if chess_board[row][position] == "K":
            return True
        elif chess_board[row][position] == "Q":
            break


winning_queens = []
for queen in queens_locations:
    res = queen_attack(queen[0], queen[1])
    if res:
        winning_queens.append(queen)

if winning_queens:
    for queen in winning_queens:
        print(queen)
else:
    print('The king is safe!')
