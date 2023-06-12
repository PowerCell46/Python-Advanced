matrix_size = int(input())
directions = input().split(", ")
matrix = [[el for el in input()] for row in range(matrix_size)]
squirrel_location = []

for i in range(0, len(matrix)):
    current_row = matrix[i]
    for index in range(0, len(current_row)):
        if current_row[index] == "s":
            squirrel_location.append(i)
            squirrel_location.append(index)

number_of_hazelnuts = 0

def move(current_direction):
    global number_of_hazelnuts

    current_row = squirrel_location[0]
    current_position = squirrel_location[1]

    if current_direction == "left":
        current_position -= 1
        if current_position < 0:
            return True

    elif current_direction == "right":
        current_position += 1
        if current_position == len(matrix[0]):
            return True

    elif current_direction == "up":
        current_row -= 1
        if current_row < 0:
            return True

    elif current_direction == "down":
        current_row += 1
        if current_row == len(matrix):
            return True

    current_symbol = matrix[current_row][current_position]
    if current_symbol == "h":
        number_of_hazelnuts += 1
        matrix[current_row][current_position] = "*"
        squirrel_location.clear()
        squirrel_location.append(current_row)
        squirrel_location.append(current_position)
    elif current_symbol == "*":
        squirrel_location.clear()
        squirrel_location.append(current_row)
        squirrel_location.append(current_position)
    elif current_symbol == "t":
        return False

flag = True

for direction in directions:
    res = move(direction)
    if res:
        print(f"The squirrel is out of the field.")
        flag = False
        break
    elif res == False:
        print(f'Unfortunately, the squirrel stepped on a trap...')
        flag = False
        break
    if number_of_hazelnuts == 3:
        break


if number_of_hazelnuts == 3 and flag:
    print(f'Good job! You have collected all hazelnuts!')
else:
    if flag:
        print(f'There are more hazelnuts to collect.')
print(f'Hazelnuts collected: {number_of_hazelnuts}')
