def fill_the_box(*args):
    args = list(args)
    box_height = args[0]
    box_length = args[1]
    box_width = args[2]
    box_volume = box_height * box_length * box_width
    number_of_cubes = 0
    index = 3
    while True:
        current_input = args[index]
        if current_input == "Finish":
            break
        number_of_cubes += current_input
        index += 1
    if box_volume - number_of_cubes > 0:
        return f'There is free space in the box. You could put {box_volume - number_of_cubes} more cubes.'
    else:
        return f'No more free space! You have {number_of_cubes - box_volume} more cubes.'
