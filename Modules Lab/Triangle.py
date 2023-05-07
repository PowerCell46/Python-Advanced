def print_triangle(size_of_the_triangle):
    index = 0
    while index <= size_of_the_triangle:
        current_print_list = []
        for i in range(1, index + 1):
            current_print_list.append(str(i))
        print(" ".join(current_print_list))
        index += 1
    while index > -1:
        current_print_list_2 = []
        for i in range(1, index - 1):
            current_print_list_2.append(str(i))
        print(" ".join(current_print_list_2))
        index -= 1
