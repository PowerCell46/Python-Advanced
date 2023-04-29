operations = {
    "+": lambda x, y, z: x + y + z,
    "-": lambda x, y, z: z - y - z,
    "*": lambda x, y, z: x * y * z,
    "/": lambda x, y, z: x / y / z,
}


def calculator(operator, first_num, second_num, third_num):
    if operator == '/' and second_num == 0 or third_num == 0:
        return "You cannot divide by a zero!"
    return operations[operator](first_num, second_num, third_num)
