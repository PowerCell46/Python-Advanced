rows, columns = [int(num) for num in input().split(" ")]
matrix = [[el for el in input().split(" ")] for _ in range(rows)]
counter = 0

for i in range(rows - 1):
    for index in range(columns - 1):
        current_row_first_el = matrix[i][index]
        current_row_second_el = matrix[i][index + 1]
        next_row_first_el = matrix[i + 1][index]
        next_row_second_el = matrix[i + 1][index + 1]
        if current_row_first_el == current_row_second_el == next_row_first_el == next_row_second_el:
            counter += 1

print(counter)
