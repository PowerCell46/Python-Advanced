from collections import deque

number_of_materials_for_crafting_toys = deque([int(num) for num in input().split()])
magic_level = deque([int(num) for num in input().split()])
toys = {"Doll": 150, "Wooden train": 250, "Teddy bear": 300, "Bicycle": 400}
crafted_items = {}
success = False

while number_of_materials_for_crafting_toys and magic_level:
    current_materials = number_of_materials_for_crafting_toys.pop()
    first_magic_level = magic_level.popleft()
    current_result = current_materials * first_magic_level
    if current_materials == 0 and first_magic_level == 0:
        continue
    if current_materials == 0:
        magic_level.appendleft(first_magic_level)
    if first_magic_level == 0:
        number_of_materials_for_crafting_toys.append(current_materials)

    if current_result in list(toys.values()):
        for key, value in toys.items():
            if value == current_result:
                if key not in crafted_items.keys():
                    crafted_items[key] = 1
                else:
                    crafted_items[key] += 1
        if "Doll" in crafted_items.keys() and "Wooden train" in crafted_items.keys():
            success = True
        if "Teddy bear" in crafted_items.keys() and "Bicycle" in crafted_items.keys():
            success = True
    else:
        if current_result < 0:
            number_of_materials_for_crafting_toys.append(current_materials + first_magic_level)
        elif current_result > 0:
            number_of_materials_for_crafting_toys.append((current_materials + 15))

if success:
    print(f'The presents are crafted! Merry Christmas!')
else:
    print("No presents this Christmas!")

if number_of_materials_for_crafting_toys:
    print(f'Materials left: {", ".join([str(el) for el in number_of_materials_for_crafting_toys][::-1])}')
if magic_level:
    print(f'Magic left: {", ".join([str(el) for el in magic_level])}')

crafted_items = sorted(crafted_items.items(), key= lambda x: x)
for key, value in crafted_items:
    print(f'{key}: {value}')
    
