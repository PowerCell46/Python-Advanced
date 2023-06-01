bomb_effects = [int(num) for num in input().split(", ")]
bomb_casings = [int(num) for num in input().split(", ")]
bomb_dict = {"Datura Bombs": 40, "Cherry Bombs": 60, "Smoke Decoy Bombs": 120}
created_bombs = {"Cherry Bombs": 0, "Datura Bombs": 0, "Smoke Decoy Bombs": 0}

while bomb_effects and bomb_casings:
    current_bomb_effect = bomb_effects.pop(0)
    current_bomb_casing = bomb_casings.pop()
    current_sum = current_bomb_effect + current_bomb_casing
    if current_sum in bomb_dict.values():
        for key in bomb_dict.keys():
            if bomb_dict[key] == current_sum:
                created_bombs[key] += 1
    else:
        current_bomb_casing -= 5
        bomb_effects.insert(0, current_bomb_effect)
        bomb_casings.append(current_bomb_casing)
    if created_bombs["Smoke Decoy Bombs"] >= 3 and created_bombs["Datura Bombs"] >= 3 and created_bombs["Cherry Bombs"] >= 3:
        break

if created_bombs["Smoke Decoy Bombs"] >= 3 and created_bombs["Datura Bombs"] >= 3 and created_bombs["Cherry Bombs"] >= 3:
    print(f'Bene! You have successfully filled the bomb pouch!')
else:
    print(f'You don\'t have enough materials to fill the bomb pouch.')

if bomb_effects:
    print(f'Bomb Effects: {", ".join([str(el) for el in bomb_effects])}')
else:
    print(f'Bomb Effects: empty')

if bomb_casings:
    print(f'Bomb Casings: {", ".join([str(el) for el in bomb_casings])}')
else:
    print(f'Bomb Casings: empty')

for key in created_bombs.keys():
    print(f'{key}: {created_bombs[key]}')
