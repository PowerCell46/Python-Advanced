milligrams_of_caffeinе = [int(num) for num in input().split(", ")]
energy_drinks = [int(num) for num in input().split(", ")]
current_energy = 0

while True:
    if len(milligrams_of_caffeinе) == 0 and len(energy_drinks) == 0:
        break

    if len(milligrams_of_caffeinе) == 0:
        break
    current_caffeine = milligrams_of_caffeinе.pop()

    if len(energy_drinks) == 0:
        break
    current_energy_drink = energy_drinks.pop(0)
    current_result = current_caffeine * current_energy_drink
    if current_energy + current_result <= 300:
        current_energy += current_result
    else:
        energy_drinks.append(current_energy_drink)
        current_energy -= 30
        if current_energy < 0:
            current_energy = 0

if len(energy_drinks) > 0:
    print(f'Drinks left: {", ".join([str(el) for el in energy_drinks])}')
else:
    print(f'At least Stamat wasn\'t exceeding the maximum caffeine.')

print(f'Stamat is going to sleep with {current_energy} mg caffeine.')
