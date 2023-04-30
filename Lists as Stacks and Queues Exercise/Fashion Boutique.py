sequence_of_numbers = [int(number) for number in input().split(" ")]
capacity_for_one_rack = int(input())
number_of_used_racks = 0
current_rack_free_space = 0
for i in range(len(sequence_of_numbers) -1, -1, -1):
    if current_rack_free_space == 0:
        number_of_used_racks += 1
        current_rack_free_space = capacity_for_one_rack
    current_number_of_clothes = sequence_of_numbers[i]
    if current_rack_free_space - current_number_of_clothes >= 0:
        current_rack_free_space -= current_number_of_clothes
    else:
        number_of_used_racks += 1
        current_rack_free_space = capacity_for_one_rack - current_number_of_clothes

print(number_of_used_racks)
