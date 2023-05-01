car_numbers = {}
number_of_commands = int(input())
while number_of_commands > 0:
    number_of_commands -= 1
    current_command, car_plate = input().split(", ")
    if current_command == "IN":
        car_numbers[car_plate] = "$"
    else:
        if car_plate in car_numbers.keys():
            del car_numbers[car_plate]

if len(car_numbers) == 0:
    print("Parking Lot is Empty")
else:
    for plate in car_numbers.keys():
        print(plate)
