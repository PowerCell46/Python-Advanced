def person_movement_function(direction):
    def valid_position(new_row, new_column):
        new_position_symbol = matrix[new_row][new_column]
        if new_position_symbol == "B":
            matrix[current_person_location[0]][current_person_location[1]] = "."
            current_person_location.clear()
            current_person_location.append(new_row)
            current_person_location.append(new_column)
            return False

        elif new_position_symbol == ".":
            matrix[current_person_location[0]][current_person_location[1]] = "."
            matrix[new_row][new_column] = "P"
            current_person_location.clear()
            current_person_location.append(new_row)
            current_person_location.append(new_column)

    current_row = current_person_location[0]
    current_column = current_person_location[1]

    if direction == "L":
        current_column -= 1
        if current_column > -1:
            valid_position_result = valid_position(current_row, current_column)
            if valid_position_result == False:
                return False
        else:
            matrix[current_person_location[0]][current_person_location[1]] = "."
            return True

    elif direction == "R":
        current_column += 1
        if current_column < len(matrix[0]):
            valid_position_result = valid_position(current_row, current_column)
            if valid_position_result == False:
                return False
        else:
            matrix[current_person_location[0]][current_person_location[1]] = "."
            return True

    elif direction == "U":
        current_row -= 1
        if current_row > -1:
            valid_position_result = valid_position(current_row, current_column)
            if valid_position_result == False:
                return False
        else:
            matrix[current_person_location[0]][current_person_location[1]] = "."
            return True

    elif direction == "D":
        current_row += 1
        if current_row < len(matrix):
            valid_position_result = valid_position(current_row, current_column)
            if valid_position_result == False:
                return False
        else:
            matrix[current_person_location[0]][current_person_location[1]] = "."
            return True


def spreading_bunnies():
    bunnie_killed_the_character = False
    def valid_bunny_position(new_row, new_column):
        new_position_symbol = matrix[new_row][new_column]
        if new_position_symbol == "P":
            matrix[new_row][new_column] = "B"
            return True
        elif new_position_symbol == ".":
            matrix[new_row][new_column] = "B"

    for bunny in bunnies_locations:
        current_row = bunny[0]
        current_column = bunny[1]
        if current_column + 1 < len(matrix[0]):  # Current row next position
            valid_bunny_result = valid_bunny_position(current_row, (current_column + 1))
            if valid_bunny_result:
                bunnie_killed_the_character = True
        if current_column - 1 > -1:  # Current row previous position
            valid_bunny_result = valid_bunny_position(current_row, (current_column -1))
            if valid_bunny_result:
                bunnie_killed_the_character = True

        if current_row + 1 < len(matrix):
            valid_bunny_result = valid_bunny_position((current_row + 1), current_column)  # Next row current position
            if valid_bunny_result:
                bunnie_killed_the_character = True
            # if current_column + 1 < len(matrix[0]):  # Next row next position
            #     valid_bunny_result = valid_bunny_position((current_row + 1), (current_column + 1))
            #     if valid_bunny_result:
            #         bunnie_killed_the_character = True
            # if current_column - 1 > -1:  # Next row previous position
            #     valid_bunny_result = valid_bunny_position((current_row + 1), (current_column - 1))
            #     if valid_bunny_result:
            #         bunnie_killed_the_character = True

        if current_row - 1 > -1:
            valid_bunny_result = valid_bunny_position((current_row - 1), current_column) # Previous row current position
            if valid_bunny_result:
                bunnie_killed_the_character = True
            # if current_column + 1 < len(matrix[0]):  # Previous row next position
            #     valid_bunny_result = valid_bunny_position((current_row - 1), (current_column + 1))
            #     if valid_bunny_result:
            #         bunnie_killed_the_character = True
            # if current_column - 1 > -1:  # Previous row previous position
            #     valid_bunny_result = valid_bunny_position((current_row - 1), (current_column - 1))
            #     if valid_bunny_result:
            #         bunnie_killed_the_character = True

    if bunnie_killed_the_character:
        return True


def bunnies_locations_func():
    bunnies_locations.clear()
    for i in range(len(matrix)):
        row1 = matrix[i]
        for index in range(len(row1)):
            if row1[index] == "B":
                bunnies_locations.append([i, index])
            elif row1[index] == "P":
                current_person_location.append(i)
                current_person_location.append(index)


rows, columns = [int(num) for num in input().split()]
matrix = [[el for el in list(input())] for _ in range(rows)]
commands = list(input())
current_person_location = []
bunnies_locations = []
bunnies_locations_func()

for command in commands:
    current_movement_result = person_movement_function(command)
    current_spreading = spreading_bunnies()
    bunnies_locations_func()

    if current_spreading or current_movement_result == False:
        for row in matrix:
            print("".join(row))
        print(f'dead: {current_person_location[0]} {current_person_location[1]}')
        break

    if current_movement_result:
        for row in matrix:
            print("".join(row))
        print(f'won: {current_person_location[0]} {current_person_location[1]}')
        break
