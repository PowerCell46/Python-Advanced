robots = input().split(";")
robots_dict = {}
seconds_list = []
counters_list = []


def printing_func(robot_name, product, time_list):
    hours = str(time_list[0])
    minutes = str(time_list[1])
    seconds = str(time_list[2])
    if len(hours) == 1:
        hours = "0" + hours
    if len(minutes) == 1:
        minutes = "0" + minutes
    if len(seconds) == 1:
        seconds = "0" + seconds
    return f'{robot_name} - {product} [{hours}:{minutes}:{seconds}]'


for index in range(0, len(robots)):
    i = robots[index]
    i = i.split("-")
    robots_dict[index] = {}
    robots_dict[index][i[0]] = int(i[1])
    seconds_list.append(int(i[1]))
    counters_list.append(0)

time = [int(time) for time in input().split(":")]
items = []

while True:
    current_input = input()
    if current_input == "End":
        break
    items.append(current_input)

while len(items):
    time[2] += 1
    if time[2] == 60:
        time[2] = 0
        time[1] += 1
        if time[1] == 60:
            time[1] = 0
            time[0] += 1
            if time[0] == 24:
                time[0] = 0

    current_item = items[0]
    taken = False
    for i in range(0, len(counters_list)):
        if counters_list[i] > 0:
            counters_list[i] -= 1 # намаляваме секундите с единица ако са по-големи от 0
        if counters_list[i] == 0 and taken == False: # ако са нула и не е взет вече продукт
            robot = list(robots_dict[i])[0]
            print(printing_func(robot, current_item, time))
            taken = True
            items.pop(0)
            counters_list[i] = seconds_list[i]
    if taken == False: # ако продулт не е взет, го слагаме отзад на опашката
        current_item = items.pop(0)
        items.append(current_item)
        
