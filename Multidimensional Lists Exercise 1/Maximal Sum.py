def current_calculation(row_index, column_index):
    current_row_first_el = matrix[row_index][column_index]
    current_row_second_el = matrix[row_index][column_index + 1]
    current_row_third_el = matrix[row_index][column_index + 2]

    next_row_first_el = matrix[row_index + 1][column_index]
    next_row_second_el = matrix[row_index + 1][column_index + 1]
    next_row_third_el = matrix[row_index + 1][column_index + 2]

    next_next_row_first_el = matrix[row_index + 2][column_index]
    next_next_row_second_el = matrix[row_index + 2][column_index + 1]
    next_next_row_third_el = matrix[row_index + 2][column_index + 2]

    current_sum = current_row_first_el + current_row_second_el + current_row_third_el + next_row_first_el + next_row_second_el + next_row_third_el + next_next_row_first_el + next_next_row_second_el + next_next_row_third_el
    if current_sum > list(biggest_sum.keys())[0]:
        del biggest_sum[list(biggest_sum.keys())[0]]
        biggest_sum[current_sum] = f'{current_row_first_el} {current_row_second_el} {current_row_third_el}\n{next_row_first_el} {next_row_second_el} {next_row_third_el}\n{next_next_row_first_el} {next_next_row_second_el} {next_next_row_third_el}'


rows, columns = [int(num) for num in input().split(" ")]
matrix = [[int(num) for num in input().split(" ")] for _ in range(rows)]
biggest_sum = {-500: 0}

for i in range(rows - 2):
    for index in range(columns - 2):
        current_calculation(i, index)

print(f'Sum = {list(biggest_sum.keys())[0]}\n{list(biggest_sum.values())[0]}')
