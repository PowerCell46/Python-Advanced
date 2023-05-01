def print_count(number):
    return f'{number:.1f} - {numbers.count(number)} times'


numbers = [float(number) for number in input().split(" ")]
checked = []
for num in numbers:
    if num not in checked:
        print(print_count(num))
        checked.append(num)
