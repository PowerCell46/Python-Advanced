rows_and_columns_length = int(input())
matrix = [[char for char in list(input())] for _ in range(rows_and_columns_length)]

searched_character = input()
coordinate = {}

for i in range(len(matrix)):
    current_row = matrix[i]
    for index in range(len(current_row)):
        if current_row[index] == searched_character:
            coordinate[i] = index
            
if len(list(coordinate.keys())) > 0:
    print(f'({list(coordinate.keys())[0]}, {coordinate[list(coordinate.keys())[0]]})')
else:
    print(f'{searched_character} does not occur in the matrix')
