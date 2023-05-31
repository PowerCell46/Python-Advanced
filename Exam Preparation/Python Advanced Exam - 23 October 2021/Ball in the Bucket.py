matrix = [[el for el in input().split(" ")] for i in range(6)]
number_of_points = 0


def shoot(current_row, current_column):
    global number_of_points

    if current_row < len(matrix) and current_column < len(matrix[0]):
        current_symbol = matrix[current_row][current_column]
        if current_symbol == "B":
            current_sum = 0
            for row1 in matrix:
                if row1[current_column] != "B" and row1[current_column] != "F":
                    current_sum += int(row1[current_column])
            matrix[current_row][current_column] = "F"
            number_of_points += current_sum


for i in range(3):
    current_coordinates = [el for el in input()]
    current_coordinates.pop(0)
    current_coordinates.pop()
    current_coordinates = "".join(current_coordinates)
    current_coordinates = current_coordinates.split(", ")
    row = int(current_coordinates[0])
    column = int(current_coordinates[1])
    shoot(row, column)

if number_of_points > 99 and number_of_points < 200:
    print(f"Good job! You scored {number_of_points} points, and you've won Football.")
elif number_of_points > 199 and number_of_points < 300:
    print(f"Good job! You scored {number_of_points} points, and you've won Teddy Bear.")
elif number_of_points > 299:
    print(f"Good job! You scored {number_of_points} points, and you've won Lego Construction Set.")
else:
    print(f"Sorry! You need {100 - number_of_points} points more to win a prize.")
