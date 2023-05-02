import math

string_expression = input().split(" ")
numbers = []

for element in string_expression:
    if element == "+":
        result = sum(numbers)
        numbers = [result]

    elif element == "-":
        result = numbers[0]
        for i in range(1, len(numbers)):
            result -= numbers[i]
        numbers = [result]

    elif element == "*":
        result = 1
        for num in numbers:
            result *= num
        numbers = [result]

    elif element == "/":
        result = numbers[0]
        for i in range(1, len(numbers)):
            result /= numbers[i]
        numbers = [math.floor(result)]

    else:
        numbers.append(int(element))

print(numbers[0])
