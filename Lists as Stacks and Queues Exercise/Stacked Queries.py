stack = []
number_of_lines = int(input())
while number_of_lines > 0:
    number_of_lines -= 1
    current_input = input()
    if "1" in current_input:
        current_input = current_input.split(" ")
        stack.append(int(current_input[1]))
    elif current_input == "2":
        if len(stack) > 0:
            stack.pop()
    elif current_input == "3":
        if len(stack) > 0:
            print(max(stack))
    elif current_input == "4":
        if len(stack) > 0:
            print(min(stack))

if len(stack) > 0:
    print(", ".join([str(number) for number in stack][::-1]))
