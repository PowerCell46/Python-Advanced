number_of_students = int(input())
grades_dictionary = {}
while number_of_students > 0:
    number_of_students -= 1
    name, grade = input().split(" ")
    if name not in grades_dictionary.keys():
        grades_dictionary[name] = [f'{float(grade):.2f}']
    else:
        grades_dictionary[name].append(f'{float(grade):.2f}')

for student, grades in grades_dictionary.items():
    print(f'{student} -> {" ".join(grades)} (avg: {(sum([float(num) for num in grades]) / len(grades)):.2f})')
