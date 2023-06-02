def list_manipulator(list_of_numbers, *args):
    position = args[1]
    if args[0] == "add":
        if position == "beginning":
            for i in range(len(args) - 1, 1, -1):
                list_of_numbers.insert(0, args[i])
        elif position == "end":
            for i in range(2, len(args)):
                list_of_numbers.append(args[i])
        return list_of_numbers

    elif args[0] == "remove":
        try:
            number_of_removals = args[2]
            if position == "beginning":
                while number_of_removals > 0:
                    number_of_removals -= 1
                    list_of_numbers.pop(0)
            elif position == "end":
                while number_of_removals > 0:
                    number_of_removals -= 1
                    list_of_numbers.pop()

        except IndexError:
            if position == "beginning":
                list_of_numbers.pop(0)
            elif position == "end":
                list_of_numbers.pop()
        return list_of_numbers
