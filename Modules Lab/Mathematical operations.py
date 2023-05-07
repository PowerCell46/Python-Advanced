def mathematical_operations(first_num, operator, second_num):
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
        }
    print(operations[operator](first_num, second_num))
    
