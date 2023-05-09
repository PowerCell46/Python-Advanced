def swap_matrix_values(row1, column1, row2, column2):
    if row1 < len(matrix) and row2 < len(matrix) and column1 < len(matrix[0]) and column2 < len(matrix[0]):
        matrix[row1][column1], matrix[row2][column2] = matrix[row2][column2], matrix[row1][column1]
        for row in matrix:
            print(" ".join([str(num) for num in row]))
    else:
        print('Invalid input!')


rows, columns = [int(num) for num in input().split(" ")]
matrix = [[num for num in input().split(" ")] for _ in range(rows)]

while True:
    current_input = input().split(" ")
    if current_input[0] == "END":
        break
    elif current_input[0] == "swap" and len(current_input) == 5:
        row_1 = int(current_input[1])
        col_1 = int(current_input[2])
        row_2 = int(current_input[3])
        col_2 = int(current_input[4])
        swap_matrix_values(row_1, col_1, row_2, col_2)
    else:
        print('Invalid input!')
