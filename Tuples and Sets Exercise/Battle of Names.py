number_of_lines = int(input())
current_row = 0
even_results = []
odd_results = []

while number_of_lines > 0:
    number_of_lines -= 1
    current_row += 1
    current_name = input()
    current_result = 0
    for letter in current_name:
        current_result += ord(letter)
    current_result = current_result // current_row
    if current_result % 2 == 0:
        even_results.append(int(current_result))
    else:
        odd_results.append(int(current_result))

even_results = {num for num in even_results}
odd_results = {num for num in odd_results}

if sum(even_results) == sum(odd_results):
    print(", ".join(str(num) for num in even_results.union(odd_results)))

elif sum(odd_results) > sum(even_results):
    print(", ".join([str(num) for num in odd_results.difference(even_results)]))

elif sum(even_results) > sum(odd_results):
    print(", ".join([str(num) for num in even_results.symmetric_difference(odd_results)]))
