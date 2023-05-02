number_of_input_lines = int(input())
chemical_compounds = {}

while number_of_input_lines > 0:
    number_of_input_lines -= 1
    current_input = input().split(" ")
    for element in current_input:
        chemical_compounds[element] = "chemical element"

print("\n".join(sorted(chemical_compounds.keys(), key=lambda x: x)))
