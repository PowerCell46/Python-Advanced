def miner_movement_function(direction):
    def valid_position_func(row, column):
        symbol = matrix[row][column]
        current_position.clear()
        current_position.append(row)
        current_position.append(column)
        if symbol == "c":
            list_counting_the_number_of_collected_coals.append("c")
            list_counting_the_number_of_current_coals.pop()
            matrix[row][column] = "*"
            if len(list_counting_the_number_of_current_coals) == 0:
                print(f'You collected all coal! ({row}, {column})')
                list_indicating_if_an_event_has_happened_or_not.append("something happened")
                return False
        elif symbol == "e":
            print(f'Game over! ({row}, {column})')
            list_indicating_if_an_event_has_happened_or_not.append("something happened")
            return False

    if direction == "left":
        new_row, new_column = [current_position[0], (current_position[1] - 1)]
        if new_column > -1:
            valid_position_result = valid_position_func(new_row, new_column)
            if valid_position_result == False:
                return False

    elif direction == "right":
        new_row, new_column = [current_position[0], (current_position[1] + 1)]
        if new_column < len(matrix[0]):
            valid_position_result = valid_position_func(new_row, new_column)
            if valid_position_result == False:
                return False

    elif direction == "up":
        new_row, new_column = [(current_position[0] - 1), current_position[1]]
        if new_row > -1:
            valid_position_result = valid_position_func(new_row, new_column)
            if valid_position_result == False:
                return False

    elif direction == "down":
        new_row, new_column = [(current_position[0] + 1), current_position[1]]
        if new_row < len(matrix):
            valid_position_result = valid_position_func(new_row, new_column)
            if valid_position_result == False:
                return False


field_size = int(input())
commands = [command for command in input().split()]
matrix = [[sym for sym in input().split()] for _ in range(field_size)]

current_position = []
list_counting_the_number_of_current_coals = []
for i in range(len(matrix)):
    row = matrix[i]
    for el in row:
        if el == "c":
            list_counting_the_number_of_current_coals.append("c")
            
    if "s" in row:
        current_position.append(i)
        current_position.append(row.index('s'))

list_counting_the_number_of_collected_coals = []
list_indicating_if_an_event_has_happened_or_not = []

for command in commands:
    if len(list_counting_the_number_of_current_coals) == 0:
        break
    miner_movement_result = miner_movement_function(command)
    if miner_movement_result == False:
        break

if len(list_indicating_if_an_event_has_happened_or_not) == 0:
    print(f'{len(list_counting_the_number_of_current_coals)} pieces of coal left. ({current_position[0]}, {current_position[1]})')
