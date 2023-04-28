def even_odd(*args):
    args = list(args)
    command = args.pop()
    if command == "even":
        return [number for number in args if number % 2 == 0]
    elif command == "odd":
        return [number for number in args if number % 2 != 0]
