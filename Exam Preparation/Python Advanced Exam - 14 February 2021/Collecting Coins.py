import math

matrix_size = int(input())
matrix = [[el for el in input().split(" ")] for i in range(matrix_size)]
player_location = []
collected_coins = 0

for row in matrix:
    if "P" in row:
        player_location = [[matrix.index(row), row.index("P")]]

def move(direction):
    global collected_coins

    current_row = player_location[-1][0]
    current_column = player_location[-1][1]
    matrix[current_row][current_column] = 0
    if direction == "up":
        current_row -= 1
        if current_row == -1:
            current_row = matrix_size - 1
    elif direction == "down":
        current_row += 1
        if current_row == matrix_size:
            current_row = 0
    elif direction == "left":
        current_column -= 1
        if current_column == -1:
            current_column = matrix_size - 1
    elif direction == "right":
        current_column += 1
        if current_column == matrix_size:
            current_column = 0

    current_symbol = matrix[current_row][current_column]
    if current_symbol == "X":
        collected_coins /= 2
        player_location.append([current_row, current_column])
        return True
    else:
        collected_coins += int(current_symbol)
        player_location.append([current_row, current_column])
        matrix[current_row][current_column] = "P"


while True:
    current_input = input()
    if current_input == "up" or current_input == "down" or current_input == "left" or current_input == "right":
        res = move(current_input)
        if res:
            print(f'Game over! You\'ve collected {math.floor(float(collected_coins))} coins.')
            break
        if float(collected_coins) >= 100:
            print(f'You won! You\'ve collected {math.floor(float(collected_coins))} coins.')
            break

print(f'Your path:')
for row in player_location:
    print(row)
