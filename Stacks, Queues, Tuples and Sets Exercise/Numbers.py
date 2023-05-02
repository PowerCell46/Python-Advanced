first_sequence = {int(num) for num in input().split(' ')}
second_sequence = {int(num) for num in input().split(" ")}
number_of_lines = int(input())

while number_of_lines > 0:
    number_of_lines -= 1
    current_input = input().split(" ")
    if current_input[0] == "Add":

        if current_input[1] == "First":
            first_sequence = list(first_sequence)
            for i in range(2, len(current_input)):
                num = int(current_input[i])
                first_sequence.append(num)
            first_sequence = set(first_sequence)

        elif current_input[1] == "Second":
            second_sequence = list(second_sequence)
            for i in range(2, len(current_input)):
                num = int(current_input[i])
                second_sequence.append(num)
            second_sequence = set(second_sequence)

    elif current_input[0] == "Remove":

        if current_input[1] == "First":
            first_sequence = list(first_sequence)
            for i in range(2, len(current_input)):
                num = int(current_input[i])
                if num in first_sequence:
                    search_index = first_sequence.index(num)
                    first_sequence.pop(search_index)

        elif current_input[1] == "Second":
            second_sequence = list(second_sequence)
            for i in range(2, len(current_input)):
                num = int(current_input[i])
                if num in second_sequence:
                    search_index = second_sequence.index(num)
                    second_sequence.pop(search_index)

    elif current_input[0] == "Check":
        first_sequence = set(first_sequence)
        second_sequence = set(second_sequence)
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

first_sequence = set(first_sequence)
second_sequence = set(second_sequence)
print(", ".join([str(num) for num in sorted(first_sequence, key=lambda x: x)]))
print(", ".join([str(num) for num in sorted(second_sequence, key=lambda x: x)]))
