number_of_names = int(input())
names = []

while number_of_names > 0:
    number_of_names -= 1
    names.append(input())
print("\n".join(set(names)))
