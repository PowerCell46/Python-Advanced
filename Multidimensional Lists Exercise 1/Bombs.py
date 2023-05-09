def bomb_function(row, column):
    current_bomb_value = matrix[row][column]
    if current_bomb_value > 0:
        matrix[row][column] = 0
        if column + 1 < len(matrix[row]):  # Current row next element
            if matrix[row][column + 1] > 0:
                matrix[row][column + 1] -= current_bomb_value
        if column - 1 >= 0:  # Current row previous element
            if matrix[row][column - 1] > 0:
                matrix[row][column - 1] -= current_bomb_value

        if row - 1 >= 0:  # For the previous row
            if matrix[row - 1][column] > 0:
                matrix[row - 1][column] -= current_bomb_value  # Previous row current element
            if column + 1 < len(matrix[row]):  # Previous row next element
                if matrix[row - 1][column + 1] > 0:
                    matrix[row - 1][column + 1] -= current_bomb_value
            if column - 1 >= 0:  # Previous row previous element
                if matrix[row - 1][column - 1] > 0:
                    matrix[row - 1][column - 1] -= current_bomb_value

        if row + 1 < len(matrix):  # For the next row
            if matrix[row + 1][column] > 0:
                matrix[row + 1][column] -= current_bomb_value  # Next row current element
            if column + 1 < len(matrix[row]):  # Next row next element
                if matrix[row + 1][column + 1] > 0:
                    matrix[row + 1][column + 1] -= current_bomb_value
            if column - 1 >= 0:  # Next row previous element
                if matrix[row + 1][column - 1] > 0:
                    matrix[row + 1][column - 1] -= current_bomb_value


rows = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(rows)]
indexes = input().split()

for coordinate in indexes:
    row, column = [int(num) for num in coordinate.split(",")]
    bomb_function(row, column)

alive_cells = 0
sum = 0
for row in matrix:
    for el in row:
        if el > 0:
            sum += el
            alive_cells += 1
print(f'Alive cells: {alive_cells}\nSum: {sum}')
for row in matrix:
    print(" ".join([str(el) for el in row]))
