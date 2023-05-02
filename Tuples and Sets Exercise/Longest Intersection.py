number_of_input_lines = int(input())
intersections_dictionary = {0: 0}

while number_of_input_lines > 0:
    number_of_input_lines -= 1
    current_input = input().split("-")
    first_half = [int(num) for num in current_input[0].split(",")]
    second_half = [int(num) for num in current_input[1].split(",")]
    first_range = []
    for number in range(first_half[0], first_half[1] + 1):
        first_range.append(number)
    first_range = set(first_range)
    second_range = []
    for number in range(second_half[0], second_half[1] + 1):
        second_range.append(number)
    second_range = set(second_range)
    current_intersection = first_range.intersection(second_range)
    if len(current_intersection) > max(intersections_dictionary.keys()):
        intersections_dictionary[len(current_intersection)] = list(current_intersection)

intersections_dictionary = sorted(intersections_dictionary.items(), key=lambda x: -x[0])
print(f'Longest intersection is {intersections_dictionary[0][1]} with length {intersections_dictionary[0][0]}')
