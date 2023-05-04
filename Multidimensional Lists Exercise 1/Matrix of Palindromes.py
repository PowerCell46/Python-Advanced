rows, columns = [int(num) for num in input().split(" ")]


for row in range(rows):
    current_row = []
    for column in range(columns):
        current_row.append(chr(97 + row) + chr(97 + column + row) + chr(97 + row))
    print(" ".join(current_row))
