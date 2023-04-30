names = []
while True:
    current_input = input()
    if current_input == "Paid":
        while len(names) > 0:
            print(names.pop(0))
    elif current_input == "End":
        print(f'{len(names)} people remaining.')
        break
    else:
        names.append(current_input)
