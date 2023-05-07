def fibonacci_sequence(*args):
    if args[0] == "Create":
        sequence = [0, 1]
        while len(sequence) < int(args[1]):
            sequence.append((sequence[-1]) + sequence[-2])
        return " ".join([str(num) for num in sequence])
    elif args[0] == "Locate":
        searched_num = args[1]
        lst = [int(num) for num in args[2].split(" ")]
        if searched_num in lst:
            return f'The number {searched_num} is at index {lst.index(searched_num)}'
        else:
            return f'The number {searched_num} is not in the sequence'

from examples import fibonacci_sequence

while True:
    current_input = input("Enter command and a number: ")
    if current_input == "Stop":
        print(f'Thanks for using the Fibonacci sequence generator!')
        break
    current_input = current_input.split()
    if current_input[0] == "Create":
        print(fibonacci_sequence(current_input[0], int(current_input[2])))
    elif current_input[0] == "Locate":
        print(fibonacci_sequence(current_input[0], int(current_input[1]), current_input[2]))
