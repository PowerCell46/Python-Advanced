num_of_people = int(input())
people = []
while num_of_people > 0:
    num_of_people -= 1
    people.append(input())
print("\n".join(set(people)))
