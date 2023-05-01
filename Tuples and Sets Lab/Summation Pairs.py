sequence_of_numbers = [int(number) for number in input().split(" ")]
target_number = int(input())
for i in range(0, len(sequence_of_numbers)):
    if i + 1 < len(sequence_of_numbers):
        for index in range(i+1, len(sequence_of_numbers)):
            if sequence_of_numbers[i] + sequence_of_numbers[index] == target_number:
                print(f'{sequence_of_numbers[i]} + {sequence_of_numbers[index]} = {target_number}')
