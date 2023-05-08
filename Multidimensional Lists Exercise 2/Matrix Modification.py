rows = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(rows)]

while True:
    current_input = input()
    if current_input == "END":
        break
    current_input = current_input.split()
    if current_input[0] == "Add":
        current_input.pop(0)
        current_row, current_column, current_value = [int(num) for num in current_input]
        if current_row < len(matrix) and current_column < len(matrix[0]) and current_row > -1 and current_column > -1:
            matrix[current_row][current_column] += current_value
        else:
            print("Invalid coordinates")

    elif current_input[0] == "Subtract":
        current_input.pop(0)
        current_row, current_column, current_value = [int(num) for num in current_input]
        if current_row < len(matrix) and current_column < len(matrix[0]) and current_row > -1 and current_column > -1:
            matrix[current_row][current_column] -= current_value
        else:
            print("Invalid coordinates")

for row in matrix:
    print(" ".join([str(num) for num in row]))
    
    
