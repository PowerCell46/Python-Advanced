tools = [int(el) for el in input().split(" ")]
substances = [int(el) for el in input().split(" ")]
challenges = [int(el) for el in input().split(" ")]

while tools and substances:
    current_tool = tools.pop(0)
    current_substance = substances.pop()
    current_result = current_tool * current_substance
    if current_result in challenges:
        search_index = challenges.index(current_result)
        challenges.pop(search_index)
    else:
        current_tool += 1
        tools.append(current_tool)
        current_substance -= 1
        if current_substance > 0:
            substances.append(current_substance)

if challenges:
    print(f"Harry is lost in the temple. Oblivion awaits him.")
else:
    print(f"Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f'Tools: {", ".join([str(el) for el in tools])}')
if substances:
    print(f'Substances: {", ".join([str(el) for el in substances ])}')
if challenges:
    print(f'Challenges: {", ".join([str(el) for el in challenges])}')
