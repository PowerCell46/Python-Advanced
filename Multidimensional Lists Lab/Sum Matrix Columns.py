number_of_lines, number_of_columns = [int(num) for num in input().split(", ")]
matrix = [[int(el) for el in input().split(" ")] for _ in range(number_of_lines)]
#         element for element in input.split(" ")  repeat this in the range of the number of lines
for col in range(number_of_columns):
    current_sum = 0
    for num in range(number_of_lines):
        current_sum += matrix[num][col]
    print(current_sum)
    
