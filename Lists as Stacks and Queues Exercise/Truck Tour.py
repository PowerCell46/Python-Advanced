number_of_petrol_stations = int(input())  # Number of petrol stations on the track
indexes = []  # Possible valid indexes
dict = {}  # Keeping the values for later checking
for i in range(0, number_of_petrol_stations):
    petrol_fuel, kilometers = [int(num) for num in input().split(" ")]
    dict[i] = {}
    dict[i][petrol_fuel] = kilometers  # Adding to the dictionary the current values fuel and kilometers
    if petrol_fuel > kilometers:
        indexes.append(i)  # if you could start from this station, append it to the list for possible starting point

for index in indexes:
    current_dict = dict.copy()  # Making a current dictionary copy which we can change
    left_out_fuel = list(dict[index].keys())[0] - list(dict[index].values())[0]  # Calculating how much more fuel we have in the tank
    del current_dict[index]
    xedni = index
    this_is_the_index = True
    while len(current_dict) > 0: # With this cycle we move through all the stations
        xedni += 1
        if xedni not in current_dict.keys():
            xedni = 0
        current_fuel = list(current_dict[xedni].keys())[0]
        current_kilometeres = list(current_dict[xedni].values())[0]
        current_left_out_fuel = current_fuel - current_kilometeres
        if left_out_fuel + current_left_out_fuel < 0: # If we subtract the current needed fuel from the fuel we have and we have a negative number, we stop the cycle and continue with the next number
            this_is_the_index = False
            break
        left_out_fuel += current_left_out_fuel
        del current_dict[xedni]
    if this_is_the_index: # If we haven't stopped the cycle, this means that the current number is eligible to be a starting point, and the first one gets printed and the program stops
        print(index)
        break
