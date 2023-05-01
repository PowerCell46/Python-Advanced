spilled_quantity = 0
cups_capacity = [int(number) for number in input().split(" ")]
bottles_capacity = [int(number) for number in input().split(" ")]

for index in range((len(bottles_capacity) - 1), -1, -1):  # Rotating the bottles starting from the last one
    current_bottles_capacity = bottles_capacity[index]
    for i in range(0, len(cups_capacity)):  # Rotating the cups starting from the last one
        current_cups_capacity = cups_capacity[i]
        current_cups_capacity -= current_bottles_capacity
        if current_cups_capacity <= 0:
            spilled_quantity -= current_cups_capacity
            cups_capacity.pop(i)
            bottles_capacity[index] = "#"
            break
        else:
            cups_capacity[i] -= current_bottles_capacity
            bottles_capacity[index] = "#"
            break
    if len(cups_capacity) == 0:
        print_list = [str(number) for number in bottles_capacity if number != "#"][::-1]
        print(f'Bottles: {" ".join(print_list)}')
        break


if len(cups_capacity) > 0:
    cups_capacity = [str(number) for number in cups_capacity]
    print(f'Cups: {" ".join(cups_capacity)}')


print(f'Wasted litters of water: {spilled_quantity}')
