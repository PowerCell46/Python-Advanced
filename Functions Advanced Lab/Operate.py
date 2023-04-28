def operate(operator, *args):
    def addition(args):
        result = 0
        for i in args:
            result += i
        return result
    def substraction(args):
        result = args[0]
        for i in range(1, len(args)):
            result -= args[i]
        return result
    def multiplication(args):
        result = 1
        for i in args:
            result *= i
        return result
    def division(args):
        result = args[0]
        for i in range(1, len(args)):
            result /= args[i]
        return result

    if operator == "+":
        return addition(list(args))
    elif operator == "-":
        return substraction(list(args))
    elif operator == "*":
        return multiplication(list(args))
    elif operator == "/":
        return division(list(args))
    else:
        return None
