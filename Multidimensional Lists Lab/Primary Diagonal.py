number_of_lines = int(input())
matrix = [[int(el) for el in input().split(" ")] for _ in range(number_of_lines)]


def sum_of_diagonals(row=-1, column=-1, sum=0):
    row += 1
    column += 1
    if row < len(matrix) and column < len(matrix[0]):
        sum += matrix[row][column]
        return sum_of_diagonals(row, column, sum)
    else:
        return sum

print(sum_of_diagonals())



