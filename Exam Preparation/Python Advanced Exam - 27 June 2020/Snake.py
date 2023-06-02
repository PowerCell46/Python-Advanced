matrix_size = int(input())
matrix = [[el for el in input()] for row in range(matrix_size)]
snake_position = []
burrows_positions = []

for index in range(0, len(matrix)):
    row = matrix[index]
    for i in range(0, len(row)):
        if row[i] == "S":
            snake_position = [index, i]
        elif row[i] == "B":
            burrows_positions.append([index, i])
food_counter = 0


def move(direction):
    global food_counter
    global snake_position
    current_row = snake_position[0]
    current_position = snake_position[1]
    matrix[current_row][current_position] = "."
    if direction == "left":
        current_position -= 1
        if current_position < 0:
            return True
    elif direction == "right":
        current_position += 1
        if current_position == len(matrix[0]):
            return True
    elif direction == "up":
        current_row -= 1
        if current_row < 0:
            return True
    elif direction == "down":
        current_row += 1
        if current_row == len(matrix):
            return True
    current_symbol = matrix[current_row][current_position]
    if current_symbol == "*":
        matrix[current_row][current_position] = "S"
        food_counter += 1
    elif current_symbol == "B":
        matrix[current_row][current_position] = "."
        search_index = burrows_positions.index([current_row, current_position])
        burrows_positions.pop(search_index)
        current_row = burrows_positions[0][0]
        current_position = burrows_positions[0][1]
        matrix[current_row][current_position] = "S"

    snake_position = [current_row, current_position]


while True:
    current_input = input()
    res = move(current_input)
    if res:
        print(f'Game over!')
        break
    if food_counter >= 10:
        print(f'You won! You fed the snake.')
        break

print(f'Food eaten: {food_counter}')
for row in matrix:
    print("".join(row))
