def moving_alice(direction):
    def valid_position(row, column):
        new_symbol = matrix[row][column]
        if new_symbol == "R":
            matrix[row][column] = "*"
            return False
        elif new_symbol != "." and new_symbol != "*":
            matrix[row][column] = "*"
            number_of_tea_bags.append(new_symbol)
        elif new_symbol == ".":
            matrix[row][column] = "*"

    current_working_row = alice_coordinates[0]
    current_position_of_the_row = alice_coordinates[1]
    matrix[current_working_row][current_position_of_the_row] = "*"

    if direction == "left":
        current_position_of_the_row -= 1
        if current_position_of_the_row > -1:
            alice_coordinates.clear()
            alice_coordinates.append(current_working_row)
            alice_coordinates.append(current_position_of_the_row)
            valid_position_result = valid_position(current_working_row, current_position_of_the_row)
            if valid_position_result == False:
                return False
        else:
            return False

    elif direction == "right":
        current_position_of_the_row += 1
        if current_position_of_the_row < len(matrix[0]):
            alice_coordinates.clear()
            alice_coordinates.append(current_working_row)
            alice_coordinates.append(current_position_of_the_row)
            valid_position_result = valid_position(current_working_row, current_position_of_the_row)
            if valid_position_result == False:
                return False
        else:
            return False

    elif direction == "up":
        current_working_row -= 1
        if current_working_row > -1:
            alice_coordinates.clear()
            alice_coordinates.append(current_working_row)
            alice_coordinates.append(current_position_of_the_row)
            valid_position_result = valid_position(current_working_row, current_position_of_the_row)
            if valid_position_result == False:
                return False
        else:
            return False

    elif direction == "down":
        current_working_row += 1
        if current_working_row < len(matrix):
            alice_coordinates.clear()
            alice_coordinates.append(current_working_row)
            alice_coordinates.append(current_position_of_the_row)
            valid_position_result = valid_position(current_working_row, current_position_of_the_row)
            if valid_position_result == False:
                return False
        else:
            return False


rows = int(input())
matrix = [[el for el in input().split()] for _ in range(rows)]
alice_coordinates = []
number_of_tea_bags = []

for i in range(len(matrix)):
    current_row = matrix[i]
    for index in range(len(current_row)):
        current_el = current_row[index]
        if current_el == "A":
            alice_coordinates.append(i)
            alice_coordinates.append(index)
        elif current_el != "R" and current_el != ".":
            matrix[i][index] = int(current_el)

while True:
    current_direction = input()
    result_of_the_movement = moving_alice(current_direction)
    if result_of_the_movement == False:
        print(f"Alice didn't make it to the tea party.")
        break
    if sum(number_of_tea_bags) >= 10:
        print('She did it! She went to the party.')
        break

for f_row in matrix:
    print(" ".join([str(el) for el in f_row]))
