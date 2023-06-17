rows, columns = [int(el) for el in input().split(",")]
matrix = [[el for el in input()] for row in range(rows)]
mouse_location = []
danger_flag = False

for index in range(0, len(matrix)):
    current_row = matrix[index]
    for i in range(0, len(current_row)):
        if current_row[i] == "M":
            mouse_location.append(index)
            mouse_location.append(i)

def move(direction):
    row = mouse_location[0]
    column = mouse_location[1]
    if direction == "up":
        row -= 1
        if row < 0:
            return False
    elif direction == "down":
        row += 1
        if row == len(matrix):
            return False
    elif direction == "left":
        column -= 1
        if column < 0:
            return False
    elif direction == "right":
        column += 1
        if column == columns:
            return False
    current_symbol = matrix[row][column]

    if current_symbol == "C":
        matrix[mouse_location[0]][mouse_location[1]] = "*"
        matrix[row][column] = "M"
        mouse_location.clear()
        mouse_location.append(row)
        mouse_location.append(column)

    elif current_symbol == "T":
        matrix[mouse_location[0]][mouse_location[1]] = "*"
        matrix[row][column] = "M"
        mouse_location.clear()
        mouse_location.append(row)
        mouse_location.append(column)
        return True
    elif current_symbol == "@":
        pass
    elif current_symbol == "*":
        matrix[mouse_location[0]][mouse_location[1]] = "*"
        matrix[row][column] = "M"
        mouse_location.clear()
        mouse_location.append(row)
        mouse_location.append(column)


while True:
    current_input = input()
    if current_input == "danger":
        danger_flag = True
        break
    res = move(current_input)

    if res == False:
        print(f'No more cheese for tonight!')
        break
    if res:
        print(f"Mouse is trapped!")
        break

    no_more_cheese = True
    for row in matrix:
        if "C" in row:
            no_more_cheese = False
            break
    if no_more_cheese:
        print(f"Happy mouse! All the cheese is eaten, good night!")
        break
if danger_flag:
    final_no_more_cheese = True
    for row in matrix:
        if "C" in row:
            final_no_more_cheese = False
            break
    if final_no_more_cheese == False:
        print(f"Mouse will come back later!")

for row in matrix:
    print("".join(row))
