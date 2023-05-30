chess_board = [[el for el in input().split(" ")] for i in range(8)]
black_position = []
white_position = []
position_dict = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}

for row in chess_board:
    if "b" in row:
        black_position = [chess_board.index(row), row.index("b")]
    if "w" in row:
        white_position = [chess_board.index(row), row.index("w")]

index = 0
def white_move():
    left_take_row = white_position[0] - 1
    left_take_position = white_position[1] - 1
    right_take_row = white_position[0] - 1
    right_take_position = white_position[1] + 1
    if left_take_row > -1 and left_take_position > -1:
        if chess_board[left_take_row][left_take_position] == "b":
            print(f'Game over! White win, capture on {position_dict[left_take_position]}{8 - left_take_row}.')
            return True
    if right_take_row > -1 and right_take_position < len(chess_board[0]):
        if chess_board[right_take_row][right_take_position] == "b":
            print(f'Game over! White win, capture on {position_dict[right_take_position]}{8 - right_take_row}.')
            return True
    next_position = white_position[0] - 1
    if next_position == 0:
        print(f'Game over! White pawn is promoted to a queen at {position_dict[left_take_position + 1]}8.')
        return True
    else:
        white_position.clear()
        white_position.append(next_position)
        white_position.append(left_take_position + 1)
        chess_board[next_position][left_take_position + 1] = "w"
        chess_board[next_position + 1][left_take_position + 1] = "-"

def black_move():
    left_take_row = black_position[0] + 1
    left_take_position = black_position[1] + 1
    right_take_row = black_position[0] + 1
    right_take_position = black_position[1] - 1
    if left_take_row < len(chess_board) and left_take_position < len(chess_board[0]):
        if chess_board[left_take_row][left_take_position] == "w":
            print(f'Game over! Black win, capture on {position_dict[left_take_position]}{8 - left_take_row}.')
            return True
    if right_take_row < len(chess_board) and right_take_position < len(chess_board[0]):
        if chess_board[right_take_row][right_take_position] == "w":
            print(f'Game over! Black win, capture on {position_dict[right_take_position]}{8 - right_take_row}.')
            return True
    next_position = black_position[0] + 1
    if next_position == len(chess_board) - 1:
        print(f'Game over! Black pawn is promoted to a queen at {position_dict[left_take_position - 1]}1.')
        return True
    else:
        black_position.clear()
        black_position.append(next_position)
        black_position.append(left_take_position - 1)
        chess_board[next_position][left_take_position - 1] = "b"
        chess_board[next_position - 1][left_take_position - 1] = "-"

while True:
    if index % 2 == 0:
        res = white_move()
        if res:
            break
    else:
        res = black_move()
        if res:
            break
    index += 1

