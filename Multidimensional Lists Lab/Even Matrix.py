number_of_rows = int(input())
matrix = []

for i in range(number_of_rows):
    current_row = [int(num) for num in input().split(", ") if int(num) % 2 == 0]
    matrix.append(current_row)

print(matrix)
