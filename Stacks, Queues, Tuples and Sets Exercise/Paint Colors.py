from collections import deque


def add_elements(input_index, first_substring, final_substring):
    if len(first_substring) > 0:
        working_substrings.insert(input_index, first_substring)
    if len(final_substring) > 0:
        working_substrings.insert(input_index, final_substring)


working_substrings = deque(input().split())
main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]

made_colors = []

while True:
    if len(working_substrings) == 0:
        break

    first_substring = working_substrings.popleft()

    if len(working_substrings) > 0:
        final_substring = working_substrings.pop()
        current_result = first_substring + final_substring
        reversed_result = final_substring + first_substring
    else:
        final_substring = ""
        current_result = first_substring
        reversed_result = first_substring[::-1]

    if current_result in main_colors or current_result in secondary_colors:
        made_colors.append(current_result)
    elif reversed_result in main_colors or reversed_result in secondary_colors:
        made_colors.append(reversed_result)

    else:
        first_substring = list(first_substring)
        first_substring.pop()
        first_substring = "".join(first_substring)
        if len(final_substring) > 0:
            final_substring = list(final_substring)
            final_substring.pop()
            final_substring = "".join(final_substring)

        if len(working_substrings) % 2 == 0:  # If the length is an even number
            input_index = len(working_substrings) // 2
            add_elements(input_index, first_substring, final_substring)
        else:  # If the length is an odd number
            input_index = len(working_substrings) // 2 + 1
            add_elements(input_index, first_substring, final_substring)

if "orange" in made_colors:
    if "red" in made_colors and "yellow" in made_colors:
        pass
    else:
        orange_index = made_colors.index("orange")
        made_colors.pop(orange_index)
if "purple" in made_colors:
    if "red" in made_colors and "blue" in made_colors:
        pass
    else:
        purple_index = made_colors.index("purple")
        made_colors.pop(purple_index)
if "green" in made_colors:
    if "yellow" in made_colors and "blue" in made_colors:
        pass
    else:
        green_index = made_colors.index("green")
        made_colors.pop(green_index)

print(made_colors)
