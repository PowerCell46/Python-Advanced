egg_sizes = [int(num) for num in input().split(", ")]
pieces_of_paper = [int(num) for num in input().split(", ")]
number_of_eggs = 0

while egg_sizes and pieces_of_paper:
    current_egg = egg_sizes.pop(0)
    if current_egg <= 0:
        continue
    if current_egg == 13:
        pieces_of_paper[0], pieces_of_paper[len(pieces_of_paper) - 1] = pieces_of_paper[len(pieces_of_paper) - 1], pieces_of_paper[0]
        continue
    current_paper = pieces_of_paper.pop()
    current_sum = current_paper + current_egg
    if current_sum <= 50:
        number_of_eggs += 1

if number_of_eggs > 0:
    print(f'Great! You filled {number_of_eggs} boxes.')
else:
    print(f'Sorry! You couldn\'t fill any boxes!')

if egg_sizes:
    print(f'Eggs left: {", ".join([str(el) for el in egg_sizes])}')
if pieces_of_paper:
    print(f'Pieces of paper left: {", ".join([str(el) for el in pieces_of_paper])}')
