firework_effects = [int(num) for num in input().split(", ")]
explosive_power = [int(num) for num in input().split(", ")]
fireworks = {"Palm Fireworks": 0, 'Willow Fireworks': 0, "Crossette Fireworks": 0}

while firework_effects and explosive_power:
    current_firework = firework_effects.pop(0)
    if current_firework <= 0:
        continue
    current_explosive = explosive_power.pop()
    if current_explosive <= 0:
        firework_effects.insert(0, current_firework)
        continue
    current_sum = current_firework + current_explosive
    if current_sum % 3 == 0 and current_sum % 5 == 0:
        fireworks["Crossette Fireworks"] += 1
    elif current_sum % 3 == 0:
        fireworks['Palm Fireworks'] += 1
    elif current_sum % 5 == 0:
        fireworks["Willow Fireworks"] += 1
    else:
        current_firework -= 1
        firework_effects.append(current_firework)
        explosive_power.append(current_explosive)

    if fireworks["Palm Fireworks"] >= 3 and fireworks["Willow Fireworks"] >= 3 and fireworks["Crossette Fireworks"] >= 3:
        break

if fireworks["Palm Fireworks"] >= 3 and fireworks["Willow Fireworks"] >= 3 and fireworks["Crossette Fireworks"] >= 3:
    print(f'Congrats! You made the perfect firework show!')
else:
    print(f'Sorry. You can\'t make the perfect firework show.')

if firework_effects:
    print(f'Firework Effects left: {", ".join([str(el) for el in firework_effects])}')
if explosive_power:
    print(f'Explosive Power left: {", ".join([str(el) for el in explosive_power])}')

for key in fireworks.keys():
    print(f'{key}: {fireworks[key]}')
