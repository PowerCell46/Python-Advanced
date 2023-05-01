green_light = int(input())
free_window = int(input())
working_list = []
no_crash = True
passed_cars = 0

while True:
    current_input = input()
    if current_input == "END":
        break
    if current_input == "green":
        green_light_duration = green_light
        free_window_duration = free_window
        working_list = [car for car in working_list if car != ""]
        for i in range(0, len(working_list)):
            car_model_length = len(working_list[i])
            if green_light_duration - car_model_length >= 0:
                working_list[i] = ""
                passed_cars += 1
                green_light_duration -= car_model_length
            else:
                if green_light_duration > 0:
                    car_model_length -= green_light_duration
                    car_model_length -= free_window_duration
                    if car_model_length <= 0:
                        green_light_duration = 0
                        working_list[i] = ""
                        passed_cars += 1
                    else:
                        car = list(working_list[i])
                        delete_elements = green_light_duration + free_window_duration
                        while delete_elements > 0:
                            car.pop(0)
                            delete_elements -= 1
                        print(f'A crash happened!\n{working_list[i]} was hit at {car[0]}.')
                        no_crash = False
                        break
        if no_crash == False:
            break
    else:
        working_list.append(current_input)

if no_crash:
    print(f'Everyone is safe.\n{passed_cars} total cars passed the crossroads.')
