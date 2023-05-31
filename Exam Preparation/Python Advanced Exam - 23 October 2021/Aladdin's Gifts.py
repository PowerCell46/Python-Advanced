materials = [int(num) for num in input().split(" ")]
genie_magic_level = [int(num) for num in input().split(" ")]
presents = {}
made = False

while materials and genie_magic_level:
    current_material = materials.pop()
    current_magic_level = genie_magic_level.pop(0)
    current_sum = current_material + current_magic_level
    if current_sum >= 100 and current_sum < 200:
        if "Gemstone" not in presents.keys():
            presents["Gemstone"] = 1
        else:
            presents["Gemstone"] += 1
    elif current_sum > 199 and current_sum < 300:
        if "Porcelain Sculpture" not in presents.keys():
            presents["Porcelain Sculpture"] = 1
        else:
            presents["Porcelain Sculpture"] += 1
    elif current_sum > 299 and current_sum < 400:
        if "Gold" not in presents.keys():
            presents["Gold"] = 1
        else:
            presents["Gold"] += 1
    elif current_sum > 399 and current_sum < 500:
        if "Diamond Jewellery" not in presents.keys():
            presents["Diamond Jewellery"] = 1
        else:
            presents["Diamond Jewellery"] += 1
    elif current_sum < 100:
        if current_sum % 2 == 0:
            current_material *= 2
            current_magic_level *= 3
            if current_material + current_magic_level < 100:
                continue
            materials.append(current_material)
            genie_magic_level.insert(0, current_magic_level)
        else:
            current_material *= 2
            current_magic_level *= 2
            if current_material + current_magic_level < 100:
                continue
            materials.append(current_material)
            genie_magic_level.insert(0, current_magic_level)
    elif current_sum > 499:
        current_material /= 2
        current_magic_level /= 2
        if current_material + current_magic_level > 499:
            continue
        materials.append(current_material)
        genie_magic_level.insert(0, current_magic_level)


if ("Gemstone" in presents and "Porcelain Sculpture" in presents) or ("Gold" in presents and "Diamond Jewellery" in presents):
    print(f'The wedding presents are made!')
    made = True

if made == False:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f'Materials left: {", ".join([str(el) for el in materials])}')

if genie_magic_level:
    print(f'Magic left: {", ".join([str(el) for el in genie_magic_level])}')


presents_names = list(presents.keys())
presents_names = sorted(presents_names, key=lambda x: x)
for present in presents_names:
    print(f'{present}: {presents[present]}')
    
