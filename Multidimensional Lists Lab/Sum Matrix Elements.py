matrix = []
matrix_sum = 0
rows, columns = [int(num) for num in input().split(", ")]

for row in range(rows):
    current_row = [int(num) for num in input().split(", ")]
    matrix.append(current_row)
    matrix_sum += sum(current_row)

print(matrix_sum)
print(matrix)
