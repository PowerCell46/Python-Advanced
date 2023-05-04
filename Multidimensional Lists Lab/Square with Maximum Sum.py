rows, columns = [int(num) for num in input().split(", ")]
matrix = [[int(num) for num in input().split(", ")] for _ in range(rows)]
biggest_sum = {-500: 0}

for i in range(rows - 1):  # Върти редовете до предпоследния - тъй като не е инклусив крайния индекс!
    current_row = matrix[i]
    next_row = matrix[i + 1]

    for index in range(0, columns - 1):  # Върти колоните до предпоследния - тъй като не е инклусив крайния индекс!

        current_row_first_el = current_row[index]
        current_row_second_el = current_row[index+1]
        next_row_first_el = next_row[index]
        next_row_second_el = next_row[index + 1]
        sum = current_row_first_el + current_row_second_el + next_row_first_el + next_row_second_el

        if sum > list(biggest_sum.keys())[0]:
            del biggest_sum[list(biggest_sum.keys())[0]]
            biggest_sum[sum] = f'{current_row_first_el} {current_row_second_el}\n{next_row_first_el} {next_row_second_el}'

print(list(biggest_sum.values())[0])
print(list(biggest_sum.keys())[0])
