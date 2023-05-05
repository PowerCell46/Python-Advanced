import functools

numbers_list = (input()).split(", ")
result = 1
for i in range(len(numbers_list)):
    number = int(numbers_list[i])
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

print(result)

# Second way
numbers = [int(num) for num in input().split(", ")]
lower_nums = [num for num in numbers if num < 6]
bigger_nums = [num for num in numbers if 5 < num < 11]
result = functools.reduce(lambda a, b: a * b, lower_nums)
result = functools.reduce(lambda a, b: (a / b), bigger_nums, result)
print(result)
