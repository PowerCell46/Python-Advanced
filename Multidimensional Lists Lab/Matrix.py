import time

number_of_rows = int(input("How many rows do you wish your matrix to be: "))
matrix = []
number_of_columns = int(input("How many elements do you wish to have on every row: "))
first_row = []

for num in range(number_of_columns):
    first_row.append(num + 1)

matrix.append(first_row)

for i in range(1, number_of_rows):
    current_row = [(num + (i * len(first_row))) for num in first_row]
    matrix.append(current_row)


def print_func(row):
    time.sleep(0.5)
    print(*row, sep=", ", end="")
    print("")


for row in matrix:
    print_func(row)
