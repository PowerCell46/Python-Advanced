quantity_of_water = int(input())
working_list = []
started = False
while True:
    current_name = input()
    if current_name == "Start":
        started = True
    elif current_name == "End":
        print(f'{quantity_of_water} liters left')
        break
    else:
        if started == False:
            working_list.append(current_name)
        else:
            if "refill" in current_name:
                current_name = current_name.split(" ")
                quantity_of_water += int(current_name[1])
            else:
                current_persons_water = int(current_name)
                if quantity_of_water >= current_persons_water:
                    quantity_of_water -= current_persons_water
                    print(f'{working_list.pop(0)} got water')
                else:
                    print(f'{working_list.pop(0)} must wait')
